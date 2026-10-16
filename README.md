 <div align="center">

# 🚗 Vehicle Garage Management System

A Python-based application for managing vehicle records and generating garage invoices using SQLite.

<p>
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python" alt="Python"/>
  <img src="https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite" alt="SQLite"/>
  <img src="https://img.shields.io/badge/Project-Learning%20Project-green" alt="Learning Project"/>
</p>

</div>

<hr/>

<h2>📌 Introduction</h2>

<p>
The Vehicle Garage Management System is a simple Python project designed to manage vehicle information and garage spare-parts records using an SQLite database.
</p>

<p>
The project demonstrates how Python can interact with a database to store and retrieve information. It also includes an invoice module that displays spare-parts details and calculates a total amount for garage billing.
</p>

<p>
This project is useful for beginners who want to practise Python programming, SQL queries, database connectivity, functions, and modular programming.
</p>

<h2>🎯 Project Objectives</h2>

<ul>
  <li>Store and organize vehicle information.</li>
  <li>Manage database operations using Python and SQLite.</li>
  <li>Maintain spare-parts records in the database.</li>
  <li>Generate a formatted garage invoice.</li>
  <li>Display customer or vehicle-owner details on an invoice.</li>
  <li>Practise writing reusable Python functions and importing modules.</li>
</ul>

<h2>✨ Features</h2>

<ul>
  <li>Vehicle record management.</li>
  <li>SQLite database connectivity.</li>
  <li>Structured storage of vehicle information.</li>
  <li>Spare-parts information retrieval.</li>
  <li>Invoice generation with owner name and car ID.</li>
  <li>Automatic invoice date and time display.</li>
  <li>Spare-parts listing with quantity and price.</li>
  <li>Total amount display.</li>
  <li>Console-based output with a formatted invoice layout.</li>
</ul>

<h2>🧰 Technologies Used</h2>

<table>
  <thead>
    <tr>
      <th>Technology</th>
      <th>Purpose</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Python</td>
      <td>Application logic and program execution.</td>
    </tr>
    <tr>
      <td>SQLite</td>
      <td>Local database for storing vehicle and spare-parts information.</td>
    </tr>
    <tr>
      <td>sqlite3</td>
      <td>Connects Python to the SQLite database.</td>
    </tr>
    <tr>
      <td>datetime</td>
      <td>Provides the date and time displayed on invoices.</td>
    </tr>
    <tr>
      <td>Git and GitHub</td>
      <td>Version control and project hosting.</td>
    </tr>
  </tbody>
</table>

<h2>📂 Project Structure</h2>

<pre>
Vehicle_Garage_Management_System/
│
├── app.py
├── garage.py
├── invoice.py
├── Database/
│   └── vehicle_garage.db
├── .gitignore
└── README.md
</pre>

<p><em>Note: The database file may be created automatically by the application. Its actual location depends on the database path configured in garage.py. The Database folder and database file may not be present in a fresh clone until the application creates them.</em></p>

<h3>File Documentation</h3>

<table>
  <thead>
    <tr>
      <th>File</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>app.py</code></td>
      <td>Main application entry point used to run the program.</td>
    </tr>
    <tr>
      <td><code>garage.py</code></td>
      <td>Handles database connectivity and garage-related database operations, including vehicle and spare-parts records.</td>
    </tr>
    <tr>
      <td><code>invoice.py</code></td>
      <td>Contains invoice-related functions for retrieving spare-parts information and displaying a formatted bill.</td>
    </tr>
    <tr>
      <td><code>Database/vehicle_garage.db</code></td>
      <td>SQLite database file used to store application data, depending on the configured database path.</td>
    </tr>
    <tr>
      <td><code>.gitignore</code></td>
      <td>Specifies files and folders that Git should ignore.</td>
    </tr>
    <tr>
      <td><code>README.md</code></td>
      <td>Project introduction, setup instructions, features, and documentation.</td>
    </tr>
  </tbody>
</table>

<h2>⚙️ Requirements</h2>

<p>Make sure you have the following installed:</p>

<ul>
  <li>Python 3.</li>
  <li>Git, if you want to clone the repository.</li>
  <li>A terminal or code editor such as Visual Studio Code.</li>
</ul>

<p>
The project uses Python's built-in <code>sqlite3</code> and <code>datetime</code> modules. No additional package installation is normally required for these modules.
</p>

<h2>🚀 Installation and Setup</h2>

<h3>Step 1: Clone the repository</h3>

<p>Open PowerShell, Command Prompt, or a terminal and execute:</p>

<pre><code>git clone https://github.com/Akshay777-coder/Vehicle_Garage_Management_System.git</code></pre>

<h3>Step 2: Navigate to the project directory</h3>

<pre><code>cd Vehicle_Garage_Management_System</code></pre>

<h3>Step 3: Verify your Python installation</h3>

<pre><code>python --version</code></pre>

<p>On Windows, you can also use:</p>

<pre><code>py --version</code></pre>

<h3>Step 4: Run the application</h3>

<pre><code>python app.py</code></pre>

<p>Alternatively, on Windows:</p>

<pre><code>py app.py</code></pre>

<p>
Follow the instructions displayed by the program. Make sure the database initialization functions in the project have created the required tables before using database-dependent features.
</p>

<h2>🧾 Invoice Module Documentation</h2>

<p>
The <code>invoice.py</code> module adds invoice-generation functionality to the Vehicle Garage Management System. It imports the <code>garage</code> module to access the SQLite database and uses Python's <code>datetime</code> module to display the invoice date and time.
</p>

<h3>Invoice Functions</h3>

<h4>1. <code>create_invoice(car_id, owner_name)</code></h4>

<p>This function displays an invoice containing:</p>

<ul>
  <li>Vehicle Garage Management System heading.</li>
  <li>Vehicle owner's name.</li>
  <li>Car ID.</li>
  <li>Current invoice date and time.</li>
  <li>Spare-parts information associated with the supplied car ID.</li>
  <li>Quantity and price information for the listed parts.</li>
  <li>Total amount.</li>
</ul>

<p>
The function queries the <code>spare_parts</code> table using the supplied car ID. If no matching records are found, it displays a message indicating that no spare parts were found for that car.
</p>

<h4>2. <code>total()</code></h4>

<p>
This function queries the spare-parts table using SQL's <code>SUM()</code> function to calculate the sum of the stored prices. The resulting amount is used by the invoice function.
</p>

<p><strong>Important:</strong> The current total calculation sums prices from the entire <code>spare_parts</code> table rather than filtering by car ID. If you want an accurate per-vehicle invoice total, update the query to calculate the sum only for the relevant car and ensure the table schema supports that relationship.</p>

<h3>Example Invoice Layout</h3>

<pre>
********************************************************************************
                 Vehicle Garage Management System

 Owner Name:  Example Customer
 Car ID:      1
 Invoice Date: DD-MM-YYYY
 Invoice Time: HH:MM

                     Spare Part     | Quantity   | Price
                     ----------------------------------------
                     Example Part   | 2          | 500
                     ----------------------------------------

 Total Amount: 500 $
********************************************************************************
</pre>

<p><em>The values above are illustrative only. Actual output depends on the records stored in the database and the invoice code.</em></p>

<h2>🗄️ Database Documentation</h2>

<p>
The project uses SQLite, a lightweight database that stores information in a local file. Database connections and queries are managed through Python's <code>sqlite3</code> module.
</p>

<h3>Vehicle Records</h3>

<table>
  <thead>
    <tr>
      <th>Field</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>car_id</code></td>
      <td>Unique vehicle record identifier.</td>
    </tr>
    <tr>
      <td><code>make</code></td>
      <td>Vehicle manufacturer.</td>
    </tr>
    <tr>
      <td><code>model</code></td>
      <td>Vehicle model.</td>
    </tr>
    <tr>
      <td><code>year</code></td>
      <td>Vehicle manufacturing year.</td>
    </tr>
    <tr>
      <td><code>color</code></td>
      <td>Vehicle colour.</td>
    </tr>
    <tr>
      <td><code>license_plate</code></td>
      <td>Vehicle registration number.</td>
    </tr>
    <tr>
      <td><code>owner_name</code></td>
      <td>Name of the vehicle owner.</td>
    </tr>
  </tbody>
</table>

<h3>Spare-Parts Records</h3>

<p>
The invoice module reads records from the <code>spare_parts</code> table. Its current query expects a <code>car_id</code> field to identify the relevant vehicle and accesses the returned columns by their positions in each database row.
</p>

<p>
Ensure the actual table schema in <code>garage.py</code> matches the columns used by <code>invoice.py</code>. For reliable invoices, each spare-parts record should have a clearly defined relationship with the relevant vehicle.
</p>

<h2>🔄 Application Workflow</h2>

<ol>
  <li>Run <code>app.py</code>.</li>
  <li>Connect to the SQLite database through <code>garage.py</code>.</li>
  <li>Perform the vehicle or spare-parts operations supported by the application.</li>
  <li>Call the invoice functionality when a bill is required.</li>
  <li>Retrieve spare-parts records for the supplied car ID.</li>
  <li>Display the owner details, invoice date, spare-parts list, and total amount.</li>
  <li>Close the database connection after completing the operation.</li>
</ol>

<h2>🛠️ Troubleshooting</h2>

<table>
  <thead>
    <tr>
      <th>Problem</th>
      <th>Possible Solution</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Python is not recognized</td>
      <td>Install Python and configure PATH, or try <code>py app.py</code> on Windows.</td>
    </tr>
    <tr>
      <td>No such table</td>
      <td>Verify that the database initialization code creates the required tables.</td>
    </tr>
    <tr>
      <td>Unable to open database file</td>
      <td>Check the database path and ensure its parent directory exists.</td>
    </tr>
    <tr>
      <td>No spare parts found for this car</td>
      <td>Verify the car ID and confirm that matching records exist in the spare-parts table.</td>
    </tr>
    <tr>
      <td>Invoice total is incorrect</td>
      <td>Check whether the total query includes records belonging to other vehicles.</td>
    </tr>
    <tr>
      <td>Duplicate car ID error</td>
      <td>Check the primary-key configuration and avoid inserting an existing ID when it is generated automatically.</td>
    </tr>
  </tbody>
</table>

<h2>🔐 Data and Privacy</h2>

<ul>
  <li>Keep private customer information out of public repositories.</li>
  <li>Use <code>.gitignore</code> to exclude local database files when they contain sensitive data.</li>
  <li>Do not commit passwords, API keys, or other private credentials.</li>
  <li>Back up your database before making structural changes.</li>
</ul>

<h2>🔮 Future Improvements</h2>

<ul>
  <li>Calculate invoice totals separately for each vehicle.</li>
  <li>Add invoice numbers and unique invoice identifiers.</li>
  <li>Track spare-parts quantities and inventory availability.</li>
  <li>Store invoice records for later retrieval.</li>
  <li>Add tax, discounts, and labour charges.</li>
  <li>Export invoices as PDF files.</li>
  <li>Improve input validation and error handling.</li>
  <li>Build a graphical user interface for easier operation.</li>
</ul>

<h2>🤝 Contributing</h2>

<p>Suggestions and contributions are welcome.</p>

<ol>
  <li>Fork the repository.</li>
  <li>Create a new branch for your changes.</li>
  <li>Make your changes and test them.</li>
  <li>Commit your changes with a meaningful message.</li>
  <li>Push your branch and open a pull request.</li>
</ol>

<h2>👨‍💻 Author</h2>

<p>
<strong>Akshay Kumar</strong><br/>
GitHub: <a href="https://github.com/Akshay777-coder">Akshay777-coder</a>
</p>

<h2>📄 License</h2>

<p>
No license is currently specified in this documentation. Add a suitable <code>LICENSE</code> file if you intend to publish the project under an open-source license.
</p>

<hr/>

<div align="center">
  <p>Thank you for visiting the Vehicle Garage Management System!</p>
  <p>If you find this project useful, consider giving it a star on GitHub. ⭐</p>
</div>
