<p align="center">
  <img src="https://img.icons8.com/?size=512&id=55494&format=png" width="20%" alt="AUTHORIZATION_WEBSITE-logo">
</p>
<p align="center">
    <h1 align="center">AUTHORIZATION_WEBSITE</h1>
</p>
<p align="center">
    <em><code>❯ REPLACE-ME</code></em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/arvind20286/authorization_website?style=flat&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/arvind20286/authorization_website?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/arvind20286/authorization_website?style=flat&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/arvind20286/authorization_website?style=flat&color=0080ff" alt="repo-language-count">
</p>
<p align="center">
		<em>Built with the tools and technologies:</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=flat&logo=HTML5&logoColor=white" alt="HTML5">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
</p>

<br>

#####  Table of Contents

- [ Overview](#-overview)
- [ Features](#-features)
- [ Repository Structure](#-repository-structure)
- [ Modules](#-modules)
- [ Getting Started](#-getting-started)
    - [ Prerequisites](#-prerequisites)
    - [ Installation](#-installation)
    - [ Usage](#-usage)
    - [ Tests](#-tests)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)

---

##  Overview

<code>❯ This project is a web-based authentication system that supports user login via two methods: traditional email/password authentication and Google OAuth. Built using Django as the backend framework, it offers a seamless login experience and ensures secure user management. The system efficiently handles different authentication methods and stores user information in a unified database structure. This project is ideal for applications where users might prefer multiple authentication options while keeping their data safe and organized.</code>

---

##  Features

<code>❯ ## Features

- **Dual Authentication Support**:
  - Users can sign up and log in using their email and password.
  - Alternatively, users can log in using their Google account via Google OAuth.

- **Secure Password Management**:
  - Email/password users’ credentials are stored securely using hashed passwords (e.g., bcrypt).
  
- **Google OAuth Integration**:
  - Users logging in via Google can seamlessly authenticate using their Google account.
  - User profile details such as name, email, and profile picture are automatically fetched and stored.

- **Session Management**:
  - Both authentication methods maintain secure sessions, allowing users to stay logged in across multiple pages.
  
- **Unified User Management**:
  - A single database table is used to store all users, whether they log in via email or Google, keeping user data consistent and easy to manage.

- **Customizable User Profile**:
  - Users can update their profile information, such as name and profile picture (especially for Google login users).

- **Scalable and Extensible**:
  - The project is designed to be easily extendable to include more social logins or additional authentication features.</code>

---

##  Repository Structure

```sh
└── authorization_website/
    ├── README.md
    ├── auth
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── auth_app
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   ├── models.py
    │   ├── static
    │   ├── templates
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── db.sqlite3
    └── manage.py
```

---

##  Modules

<details closed><summary>.</summary>

| File | Summary |
| --- | --- |
| [db.sqlite3](https://github.com/arvind20286/authorization_website/blob/main/db.sqlite3) | <code>❯ REPLACE-ME</code> |
| [manage.py](https://github.com/arvind20286/authorization_website/blob/main/manage.py) | <code>❯ REPLACE-ME</code> |

</details>

<details closed><summary>auth_app</summary>

| File | Summary |
| --- | --- |
| [admin.py](https://github.com/arvind20286/authorization_website/blob/main/auth_app/admin.py) | <code>❯ REPLACE-ME</code> |
| [apps.py](https://github.com/arvind20286/authorization_website/blob/main/auth_app/apps.py) | <code>❯ REPLACE-ME</code> |
| [tests.py](https://github.com/arvind20286/authorization_website/blob/main/auth_app/tests.py) | <code>❯ REPLACE-ME</code> |
| [views.py](https://github.com/arvind20286/authorization_website/blob/main/auth_app/views.py) | <code>❯ REPLACE-ME</code> |
| [urls.py](https://github.com/arvind20286/authorization_website/blob/main/auth_app/urls.py) | <code>❯ REPLACE-ME</code> |
| [models.py](https://github.com/arvind20286/authorization_website/blob/main/auth_app/models.py) | <code>❯ REPLACE-ME</code> |

</details>

<details closed><summary>auth_app.templates</summary>

| File | Summary |
| --- | --- |
| [index.html](https://github.com/arvind20286/authorization_website/blob/main/auth_app/templates/index.html) | <code>❯ REPLACE-ME</code> |
| [welcome.html](https://github.com/arvind20286/authorization_website/blob/main/auth_app/templates/welcome.html) | <code>❯ REPLACE-ME</code> |

</details>

<details closed><summary>auth_app.migrations</summary>

| File | Summary |
| --- | --- |
| [0001_initial.py](https://github.com/arvind20286/authorization_website/blob/main/auth_app/migrations/0001_initial.py) | <code>❯ REPLACE-ME</code> |

</details>

<details closed><summary>auth</summary>

| File | Summary |
| --- | --- |
| [asgi.py](https://github.com/arvind20286/authorization_website/blob/main/auth/asgi.py) | <code>❯ REPLACE-ME</code> |
| [wsgi.py](https://github.com/arvind20286/authorization_website/blob/main/auth/wsgi.py) | <code>❯ REPLACE-ME</code> |
| [urls.py](https://github.com/arvind20286/authorization_website/blob/main/auth/urls.py) | <code>❯ REPLACE-ME</code> |
| [settings.py](https://github.com/arvind20286/authorization_website/blob/main/auth/settings.py) | <code>❯ REPLACE-ME</code> |

</details>

---

##  Getting Started

###  Prerequisites

**Python**: `version 3.9.1`

###  Installation

Build the project from source:

1. Clone the authorization_website repository:
```sh
❯ git clone https://github.com/arvind20286/authorization_website
```

2. Navigate to the project directory:
```sh
❯ cd authorization_website
```

3. Install the required dependencies:
```sh
❯ pip install -r requirements.txt
```

###  Usage

To run the project, execute the following command:

```sh
❯ python manage.py runserver
```

<!-- ###  Tests

Execute the test suite using the following command:

```sh
❯ pytest
```

---

##  Project Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three. -->

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/arvind20286/authorization_website/issues)**: Submit bugs found or log feature requests for the `authorization_website` project.
- **[Submit Pull Requests](https://github.com/arvind20286/authorization_website/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/arvind20286/authorization_website/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/arvind20286/authorization_website
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/arvind20286/authorization_website/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=arvind20286/authorization_website">
   </a>
</p>
</details>

---
<!-- 
##  License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

--- -->