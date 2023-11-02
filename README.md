# ALX-Holberton BnB - Airbnb Clone Project

![Optional Text](hbnb.png)

## Project Description

The ALX-Holberton B&B project is the culmination of four months of intensive study at ALX-Holberton School, focusing on full-stack software engineering. The primary goal of this project is to deploy a replica of the popular Airbnb website using a custom server. The final version of this project will include the following key components:

- A command-line interpreter for data manipulation, essential for development and debugging.
- A dynamic website with both static and interactive features.
- A robust database for managing backend functionalities.
- An API for seamless communication between the front-end and back-end systems.

## Core Concepts

Throughout this project, you will encounter essential software engineering concepts, including:

- Creating a Python package.
- Building a command-line interpreter in Python using the `cmd` module.
- Understanding unit testing and its implementation in a large-scale project.
- Serialization and deserialization of classes.
- Working with JSON files for data storage.
- Handling datetime objects.
- Utilizing UUIDs for unique identification.
- Understanding the usage of *args and **kwargs in Python functions.
- Effectively managing named arguments in functions.

## Project Structure

- The `models` directory contains all the classes used in the project, representing different objects.
- The `tests` directory houses all unit tests for the project.
- The `console.py` file serves as the entry point for the command-line interpreter.
- The `models/base_model.py` file is the base class for all models, with common attributes and methods.
- The `models/engine` directory includes various storage classes, with `file_storage.py` being the initial storage engine implemented.

## Project Phases

### Phase One

The first phase focuses on implementing a robust storage system that abstracts the storage and persistence of objects. Key tasks include:

- Implementing a parent class, `BaseModel`, responsible for object initialization, serialization, and deserialization.
- Creating a straightforward flow for serialization/deserialization: Instance ➔ Dictionary ➔ JSON string ➔ File.
- Defining classes corresponding to Airbnb entities (e.g., `User`, `State`, `City`, `Place`) that inherit from `BaseModel`.
- Developing the initial abstracted storage engine: File storage.
- Designing and conducting unit tests to validate the classes and storage engine.
- Establishing a data model for the project.
- Implementing functionality for object management, including creation, updating, and deletion, via a console/command interpreter.
- Storing and persisting objects as JSON files.

## Command Interpreter Description

Here's a summary of the commands available in the command interpreter:

- `quit`: Exits the console.
- `Ctrl+D`: Exits the console.
- `help` or `help <command>`: Displays all available commands or provides instructions for a specific command.
- `create <class>`: Creates an object of the specified class, saves it to a JSON file, and displays the object's ID.
- `show <class> <ID>`: Displays the string representation of the specified object.
- `destroy <class> <ID>`: Deletes an object.
- `all` or `all <class>`: Displays string representations of all objects or objects of a specific class.
- `update <class> <id> <attribute name> "<attribute value>"`: Updates an object with the given attribute (new or existing).
- `<class>.all()`: Equivalent to `all <class>`.
- `<class>.count()`: Retrieves the count of objects of a specific class.
- `<class>.show(<ID>)`: Equivalent to `show <class> <ID>`.
- `<class>.destroy(<ID>)`: Equivalent to `destroy <class> <ID>`.
- `<class>.update(<ID>, <attribute name>, <attribute value>`: Equivalent to `update <class> <ID> <attribute name> <attribute value>`.
- `<class>.update(<ID>, <dictionary representation>)`: Updates an object based on a dictionary representation of attribute names and values.

## General Execution

The shell can function interactively as follows:

$ ./console.py
(hbnb) help
Documented commands (type help <topic>):

EOF help quit
(hbnb)
(hbnb)
(hbnb) quit
$


It also supports non-interactive mode:

$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):

EOF help quit
(hbnb)
$


## Final Product

![Final Product Image](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/fe2e3e7701dec72ce612472dab9bb55fe0e9f6d4.png)

## Data Diagram

![Data Diagram](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/99e1a8f2be8c09d5ce5ac321e8cf39f0917f8db5.jpg)
