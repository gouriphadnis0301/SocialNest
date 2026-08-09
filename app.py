
import streamlit as st
import requests

# =========================================================
# CONFIG
# =========================================================

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="SocialNest",
    page_icon="🌐",
    layout="wide"
)


# =========================================================
# SESSION
# =========================================================

if "token" not in st.session_state:
    st.session_state.token = None

if "username" not in st.session_state:
    st.session_state.username = None


# =========================================================
# HEADERS
# =========================================================

def get_headers():
    return {
        "Authorization": f"Bearer {st.session_state.token}"
    }


# =========================================================
# REGISTER
# =========================================================

def register_user(email, password):

    try:

        response = requests.post(
            f"{API_URL}/users/",
            json={
                "email": email,
                "password": password
            }
        )

        return response

    except requests.exceptions.ConnectionError:

        return None


# =========================================================
# LOGIN
# =========================================================

def login_user(username, password):

    try:

        response = requests.post(
            f"{API_URL}/login",
            data={
                "username": username,
                "password": password
            }
        )

        if response.status_code == 200:

            data = response.json()

            st.session_state.token = data["access_token"]
            st.session_state.username = username

            return True, "Login successful!"

        return False, response.text

    except requests.exceptions.ConnectionError:

        return False, "FastAPI backend is not running."


# =========================================================
# GET ALL POSTS
# =========================================================

def get_posts():

    try:

        response = requests.get(
            f"{API_URL}/posts/",
            headers=get_headers()
        )

        if response.status_code == 200:

            return response.json()

        st.error(response.text)

        return []

    except requests.exceptions.ConnectionError:

        st.error(
            "FastAPI backend is not running."
        )

        return []


# =========================================================
# CREATE POST
# =========================================================

def create_post(title, content, published):

    try:

        response = requests.post(
            f"{API_URL}/posts/",
            json={
                "title": title,
                "content": content,
                "published": published
            },
            headers=get_headers()
        )

        return response

    except requests.exceptions.ConnectionError:

        st.error(
            "FastAPI backend is not running."
        )

        return None


# =========================================================
# GET POST BY ID
# =========================================================

def get_post_by_id(post_id):

    try:

        response = requests.get(
            f"{API_URL}/posts/{post_id}",
            headers=get_headers()
        )

        return response

    except requests.exceptions.ConnectionError:

        st.error(
            "FastAPI backend is not running."
        )

        return None


# =========================================================
# UPDATE POST
# =========================================================

def update_post(post_id, title, content, published):

    try:

        response = requests.put(
            f"{API_URL}/posts/{post_id}",
            json={
                "title": title,
                "content": content,
                "published": published
            },
            headers=get_headers()
        )

        return response

    except requests.exceptions.ConnectionError:

        st.error(
            "FastAPI backend is not running."
        )

        return None


# =========================================================
# DELETE POST
# =========================================================

def delete_post(post_id):

    try:

        response = requests.delete(
            f"{API_URL}/posts/{post_id}",
            headers=get_headers()
        )

        return response

    except requests.exceptions.ConnectionError:

        st.error(
            "FastAPI backend is not running."
        )

        return None


# =========================================================
# VOTE POST
# =========================================================

def vote_post(post_id, direction):

    try:

        response = requests.post(
            f"{API_URL}/vote/",
            json={
                "post_id": post_id,
                "dir": direction
            },
            headers=get_headers()
        )

        return response

    except requests.exceptions.ConnectionError:

        st.error(
            "FastAPI backend is not running."
        )

        return None


# =========================================================
# LOGIN / REGISTER SCREEN
# =========================================================

if not st.session_state.token:

    st.title("🌐 SocialNest")

    st.write(
        "Connect, share and interact with your community."
    )

    login_tab, register_tab = st.tabs(
        ["🔐 Login", "📝 Register"]
    )

    # =====================================================
    # LOGIN
    # =====================================================

    with login_tab:

        st.subheader("Login to SocialNest")

        with st.form("login_form"):

            username = st.text_input(
                "Email / Username"
            )

            password = st.text_input(
                "Password",
                type="password"
            )

            login_button = st.form_submit_button(
                "🔐 Login"
            )

            if login_button:

                if not username or not password:

                    st.warning(
                        "Please enter email and password."
                    )

                else:

                    success, message = login_user(
                        username,
                        password
                    )

                    if success:

                        st.success(
                            message
                        )

                        st.rerun()

                    else:

                        st.error(
                            message
                        )

    # =====================================================
    # REGISTER
    # =====================================================

    with register_tab:

        st.subheader(
            "Create a SocialNest Account"
        )

        with st.form("register_form"):

            email = st.text_input(
                "Email"
            )

            password = st.text_input(
                "Password",
                type="password"
            )

            confirm_password = st.text_input(
                "Confirm Password",
                type="password"
            )

            register_button = st.form_submit_button(
                "📝 Create Account"
            )

            if register_button:

                if not email or not password:

                    st.warning(
                        "Email and password are required."
                    )

                elif password != confirm_password:

                    st.error(
                        "Passwords do not match."
                    )

                else:

                    response = register_user(
                        email,
                        password
                    )

                    if response is None:

                        st.error(
                            "FastAPI backend is not running."
                        )

                    elif response.status_code == 201:

                        st.success(
                            "Account created successfully! "
                            "Now login with your email and password."
                        )

                    else:

                        st.error(
                            f"Registration failed: "
                            f"{response.text}"
                        )

    st.stop()


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🌐 SocialNest")

st.sidebar.write(
    f"Logged in as:"
)

st.sidebar.write(
    f"**{st.session_state.username}**"
)

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "➕ Create Post",
        "🔍 Get Post",
        "✏️ Update Post",
        "🗑️ Delete Post"
    ]
)


# =========================================================
# LOGOUT
# =========================================================

if st.sidebar.button("🚪 Logout"):

    st.session_state.token = None
    st.session_state.username = None

    st.rerun()


# =========================================================
# HOME
# =========================================================

if page == "🏠 Home":

    st.title("🏠 SocialNest Feed")

    posts = get_posts()

    if not posts:

        st.info(
            "No posts available."
        )

    else:

        for item in posts:

            # IMPORTANT:
            # Backend response is:
            #
            # {
            #     "Post": {...},
            #     "votes": 0
            # }

            post = item.get(
                "Post",
                {}
            )

            votes = item.get(
                "votes",
                0
            )

            post_id = post.get(
                "id"
            )

            title = post.get(
                "title",
                "Untitled"
            )

            content = post.get(
                "content",
                ""
            )

            published = post.get(
                "published",
                False
            )

            with st.container():

                st.subheader(
                    f"#{post_id} — {title}"
                )

                st.write(
                    content
                )

                if published:

                    st.caption(
                        "🟢 Published"
                    )

                else:

                    st.caption(
                        "⚪ Draft"
                    )

                owner = post.get(
                    "owner"
                )

                if owner:

                    st.caption(
                        f"Posted by: "
                        f"{owner.get('email', 'Unknown')}"
                    )

                st.write(
                    f"👍 Votes: {votes}"
                )

                col1, col2 = st.columns(2)

                # =========================================
                # VOTE
                # =========================================

                with col1:

                    if st.button(
                        "👍 Vote",
                        key=f"vote_{post_id}"
                    ):

                        response = vote_post(
                            post_id,
                            1
                        )

                        if response is not None:

                            if response.status_code in [200, 201]:

                                st.success(
                                    "Vote added!"
                                )

                                st.rerun()

                            else:

                                st.error(
                                    response.text
                                )

                # =========================================
                # REMOVE VOTE
                # =========================================

                with col2:

                    if st.button(
                        "👎 Remove Vote",
                        key=f"unvote_{post_id}"
                    ):

                        response = vote_post(
                            post_id,
                            0
                        )

                        if response is not None:

                            if response.status_code in [200, 201]:

                                st.success(
                                    "Vote removed!"
                                )

                                st.rerun()

                            else:

                                st.error(
                                    response.text
                                )

                st.divider()


# =========================================================
# CREATE POST
# =========================================================

elif page == "➕ Create Post":

    st.title("➕ Create a Post")

    with st.form(
        "create_post_form"
    ):

        title = st.text_input(
            "Title"
        )

        content = st.text_area(
            "Content"
        )

        published = st.checkbox(
            "Publish post",
            value=True
        )

        submit = st.form_submit_button(
            "Create Post"
        )

        if submit:

            if not title or not content:

                st.warning(
                    "Title and content are required."
                )

            else:

                response = create_post(
                    title,
                    content,
                    published
                )

                if response is not None:

                    if response.status_code == 201:

                        st.success(
                            "Post created successfully!"
                        )

                        st.json(
                            response.json()
                        )

                    else:

                        st.error(
                            response.text
                        )


# =========================================================
# GET POST BY ID
# =========================================================

elif page == "🔍 Get Post":

    st.title("🔍 Get Post by ID")

    post_id = st.number_input(
        "Post ID",
        min_value=1,
        step=1
    )

    if st.button(
        "Get Post"
    ):

        response = get_post_by_id(
            post_id
        )

        if response is not None:

            if response.status_code == 200:

                st.success(
                    "Post found!"
                )

                st.json(
                    response.json()
                )

            else:

                st.error(
                    response.text
                )


# =========================================================
# UPDATE POST
# =========================================================

elif page == "✏️ Update Post":

    st.title("✏️ Update Post")

    post_id = st.number_input(
        "Post ID",
        min_value=1,
        step=1
    )

    title = st.text_input(
        "New Title"
    )

    content = st.text_area(
        "New Content"
    )

    published = st.checkbox(
        "Published",
        value=True
    )

    if st.button(
        "Update Post"
    ):

        response = update_post(
            post_id,
            title,
            content,
            published
        )

        if response is not None:

            if response.status_code == 200:

                st.success(
                    "Post updated successfully!"
                )

                st.json(
                    response.json()
                )

            else:

                st.error(
                    response.text
                )


# =========================================================
# DELETE POST
# =========================================================

elif page == "🗑️ Delete Post":

    st.title("🗑️ Delete Post")

    post_id = st.number_input(
        "Post ID",
        min_value=1,
        step=1
    )

    if st.button(
        "🗑️ Delete Post"
    ):

        response = delete_post(
            post_id
        )

        if response is not None:

            if response.status_code in [200, 204]:

                st.success(
                    "Post deleted successfully!"
                )

            else:

                st.error(
                    response.text
                )