# Flask Bloglite (Simple blog post website)

## Setup & Installation

Just need a latest version of Python installed.

```bash
pip install -r requirements.txt
```

## Running the App

```bash
python main.py
```

## Viewing the app

Go to `http://127.0.0.1:5000`

## Folder Structure

```
.
└── ProjectFolder/
    ├── main.py
    ├── requirements.txt
    ├── README.md
    ├── Project_doc.pdf
    └── blog/
        ├── static/
        │   ├── downloaded_blogs
        │   ├── profile_pics
        │   ├── blog_pics
        │   └── images/
        │       ├── background.jpg
        │       ├── blog-default.png
        │       ├── bloglite.gif
        │       └── default_profile.png
        ├── templates/
        │   ├── 404.html
        │   ├── index_blog.html
        │   ├── login.html
        │   ├── new_post.html
        │   ├── posts.html
        │   ├── other_profile.html
        │   ├── post_restriction.html
        │   ├── post_updated.html
        │   ├── profile.html
        │   ├── register.html
        │   ├── search.html
        │   └── user_update.html
        ├── __init__.py
        ├── auth.py
        ├── models.py
        └── views.py

```

This structure clearly outlines the organization of your Flask Bloglite project. The key components are:

- **`ProjectFolder`**: The root directory of your project.
- **`main.py`**: The main entry point for running your Flask application.
- **`requirements.txt`**: Lists the Python packages required for your project.
- **`README.md`**: This file, providing information about your project.
- **`Project_doc.pdf`**: Presumably documentation related to your project.
- **`blog`**: The main package containing the core logic of your blog application.
  - **`static`**: Contains static assets like images, CSS, and JavaScript files.
    - **`downloaded_blogs`**: Likely stores downloaded blog content.
    - **`profile_pics`**: Stores user profile pictures.
    - **`blog_pics`**: Stores images related to blog posts.
    - **`images`**: Contains various images used throughout the application.
  - **`templates`**: Contains HTML templates for rendering web pages.
  - **`__init__.py`**: Initializes the `blog` package.
  - **`auth.py`**: Likely handles authentication and user management.
  - **`models.py`**: Defines the data models for your application (e.g., users, posts).
  - **`views.py`**: Contains the view functions that handle user requests and render templates.

This structure is typical for Flask applications and promotes a well-organized and maintainable codebase. Remember to replace `ProjectFolder` with the actual name of your project folder.
