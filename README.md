<div align="center">

# 🚗 Vehicle Garage Management System

<p>
  A simple Python application for managing vehicle records in a garage.
</p>

<p>
  <a href="https://github.com/Akshay777-coder/Vehicle_Garage_Management_System">
    <img src="https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github" alt="GitHub Repository">
  </a>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Database-SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
</p>

</div>

---

## 📌 Introduction

The **Vehicle Garage Management System** is a Python-based project designed to help organize vehicle information in one place. It uses **SQLite** to store vehicle records in a local database.

The project is suitable for learning Python, database operations, and how an application can connect to a database. Instead of keeping vehicle details in separate handwritten records, the application can store structured information such as the vehicle's make, model, year, colour, licence plate, and owner's name.

## ✨ Project Goals

- Store vehicle information in a structured database.
- Make vehicle records easier to organize and manage.
- Practise Python functions and database connectivity.
- Learn how to perform SQL operations with Python's built-in `sqlite3` module.

## 🧰 Technologies Used

<table>
  <thead>
    <tr>
      <th>Technology</th>
      <th>Purpose</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Python</strong></td>
      <td>Application logic and program execution.</td>
    </tr>
    <tr>
      <td><strong>SQLite</strong></td>
      <td>Stores vehicle records in a local database file.</td>
    </tr>
    <tr>
      <td><strong>sqlite3</strong></td>
      <td>Python's built-in library for working with SQLite databases.</td>
    </tr>
    <tr>
      <td><strong>Git and GitHub</strong></td>
      <td>Version control and project hosting.</td>
    </tr>
  </tbody>
</table>

## ✅ Vehicle Information

The vehicle records are designed to include the following fields:

<table>
  <thead>
    <tr>
      <th>Field</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><code>car_id</code></td><td>Unique ID for a vehicle record.</td></tr>
    <tr><td><code>make</code></td><td>Vehicle manufacturer or brand.</td></tr>
    <tr><td><code>model</code></td><td>Vehicle model name.</td></tr>
    <tr><td><code>year</code></td><td>Vehicle manufacturing year.</td></tr>
    <tr><td><code>color</code></td><td>Vehicle colour.</td></tr>
    <tr><td><code>license_plate</code></td><td>Vehicle registration or licence plate number.</td></tr>
    <tr><td><code>owner_name</code></td><td>Name of the vehicle owner.</td></tr>
  </tbody>
</table>

> **Note:** The fields and features available to you depend on the current source code in the repository. Update this section if your database schema changes.

## ⚙️ Requirements

Before running the project, install:

- Python 3.10 or a compatible Python 3 version.
- Git (required only if you want to clone the repository).
- A terminal or code editor, such as VS Code.

SQLite support is included with most standard Python installations through the `sqlite3` module, so a separate SQLite package is usually not required.

## 📥 Installation and Setup

### 1. Clone the repository

Open Command Prompt, PowerShell, or a terminal and run:

```bash
git clone https://github.com/Akshay777-coder/Vehicle_Garage_Management_System.git
```

### 2. Open the project folder

```bash
cd Vehicle_Garage_Management_System
```

### 3. (Optional) Create a virtual environment

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux / macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install dependencies

The project uses Python's built-in `sqlite3` module for SQLite database access. If the repository contains a `requirements.txt` file, install its listed packages with:

```bash
python -m pip install -r requirements.txt
```

If there is no `requirements.txt` file and the project uses only built-in Python modules, no additional packages may be needed.

## ▶️ How to Run the Application

From the project directory, run:

```bash
python app.py
```

If your system uses `python3` as the Python command, run:

```bash
python3 app.py
```

Follow the prompts or instructions displayed by the program.

**If you see `can't open file 'app.py'`:** check the filenames in the project folder. The entry-point file may have a different name; use the actual Python filename in the run command.

## 🗄️ Database Documentation

The project uses **SQLite**, a lightweight database that stores data in a local file. The database file used in the current project code is:

```text
Database/vehicle_garage.db
```

The database connection is created using Python's `sqlite3` library. SQL statements can then be used to create tables and insert or retrieve vehicle details.

### Example: Connect to the database

```python
import sqlite3

database = r"Database/vehicle_garage.db"
connection = sqlite3.connect(database)
cursor = connection.cursor()

# Run SQL statements using cursor.execute(...)

connection.commit()
connection.close()
```

> This is an illustrative connection example. Use the database path configured in your own `app.py` or database module. If your project already has a connection function, use that function instead of creating a second connection.

## 🧭 How the System Works

<ol>
  <li><strong>Start the application:</strong> Run the Python entry-point file from the project folder.</li>
  <li><strong>Connect to the database:</strong> Python connects to the SQLite database file.</li>
  <li><strong>Work with vehicle records:</strong> The program's implemented functions execute database operations for the available features.</li>
  <li><strong>Save changes:</strong> Database changes are committed so that they can be stored in the database file.</li>
  <li><strong>Close the connection:</strong> The application closes the database connection when the work is complete.</li>
</ol>

## 📂 Project Structure

The project is expected to have a structure similar to the following. Actual filenames and folders may differ:

```text
Vehicle_Garage_Management_System/
├── app.py
├── Database/
│   └── vehicle_garage.db
├── .gitignore
└── README.md
```

## 🛠️ Troubleshooting

<table>
  <thead>
    <tr>
      <th>Problem</th>
      <th>What to try</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>python is not recognized</code></td>
      <td>Install Python and enable the option to add Python to PATH, or try <code>py app.py</code> on Windows.</td>
    </tr>
    <tr>
      <td><code>can't open file 'app.py'</code></td>
      <td>Make sure your terminal is in the project directory and confirm the actual entry-point filename.</td>
    </tr>
    <tr>
      <td><code>No such table</code></td>
      <td>Check that the application creates the required table and connects to the correct database file.</td>
    </tr>
    <tr>
      <td><code>unable to open database file</code></td>
      <td>Verify the database path and make sure the parent directory exists and is writable.</td>
    </tr>
  </tbody>
</table>

## 🔒 Data and Privacy

- The SQLite database is stored locally unless the application is changed to use another database.
- Do not commit private customer information or real vehicle-owner data to a public repository.
- Keep local database files out of Git when they contain private or personal information. Use `.gitignore` where appropriate.

## 🤝 Contributing

Contributions and suggestions are welcome.

1. Fork this repository.
2. Create a branch for your change.
3. Make and test your changes.
4. Commit your changes with a clear message.
5. Open a pull request describing what you changed.

## 👨‍💻 Author

**Akshay Kumar**

- GitHub: [@Akshay777-coder](https://github.com/Akshay777-coder)
- Project repository: [Vehicle Garage Management System](https://github.com/Akshay777-coder/Vehicle_Garage_Management_System)

## 📄 License

No licence information is specified in this README. If you want others to reuse, modify, or distribute this project, consider adding a `LICENSE` file and mentioning the selected licence here.

---

<div align="center">
  <p><strong>Thank you for visiting the Vehicle Garage Management System repository!</strong></p>
  <p>If you find this project useful, consider giving the repository a ⭐ on GitHub.</p>
</div>
