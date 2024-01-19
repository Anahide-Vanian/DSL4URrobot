# Project README

## DSL for UR Robot Control

Programming robots typically requires programming expertise, creating a barrier for domain experts with no technical background in robotics. Skilled professionals lack the means to leverage robots in their domain due to a gap in programming knowledge. This project aims to bridge this gap by providing a user-friendly solution for programming robots without delving into technical intricacies.

The objective is to create a high-level domain-specific language (DSL) to control a Universal Robots (UR) robot using the Xtext framework in association with the Eclipse application. The DSL allows users to define scenarios in natural language, adhering to the syntax rules specified in the Xtext grammar file.
Using natural language simplifies robot programming and enables users without technical knowledge to configure robot behavior within their domain.


#### Overview of Technologies

The project utilizes various technologies:
- **Xtext:** Implements syntax, known for developing domain-specific languages.
- **Behavior-Driven Development (BDD) and Gherkin syntax:** Allows users to write scenarios and define robot behavior.
- **Behave:** Processes syntax and translates it into executable code.
- **ur_rtde Python library:** Enables real-time data exchange between user and robot.
- **UR robot, gripper and additional equipment:** Used for scenario execution in real-time.

### Setup Process

Follow the instructions below to set up and run the project:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/ratgen/DSLBeta1/tree/robot/dk.sdu.bdd.xtext.parent
   ```
2. **Install Eclipse:**
   - Download and install the latest version of Eclipse from [eclipse.org](https://www.eclipse.org/downloads/).

3. **Install Xtext Plugin:**
   - Open Eclipse and go to `Help -> Eclipse Marketplace`.
   - Search for "Xtext" and install the Xtext plugin.

4. **Import Project into Eclipse:**
   - Open Eclipse and choose `File -> Import -> General -> Existing Projects into Workspace`.
   - Select the cloned `DSLBeta1` project directory.
     
5. **Install Python Extensions:**

Since the project includes Python source code, ensure you have Python extensions installed. Follow these steps:
   - Open Eclipse and go to `Help -> Eclipse Marketplace`..
   - Type "PyDev" into the search bar.
   - Follow the instructions to install the PyDev plugin.
  
6. **Install Python Interpreter:**

The Python interpreter path is typically configured by default in the IDE. However, if you encounter issues related to the Python interpreter, follow these steps:

- Open Eclipse and navigate to `Window -> Preferences -> PyDev -> Interpreters -> Python Interpreter -> New`.
- Add the path to your Python installation.

7.  **Install Gherkin Syntax Extensions:**

The project involves writing files with a ".feature" extension following the Gherkin Syntax, processed by the behave framework. Make sure to install the required extensions for Gherkin Syntax by following these steps:
- Open Eclipse and navigate to `Help -> Eclipse Marketplace`.
- In the Eclipse Marketplace dialog, type "Cucumber" into the search bar.
- Locate the "Cuncumber Eclipse Plugin" plugin for Eclipse in the search results.
- Follow the instructions to install the "Cuncumber Eclipse Plugin" plugin.

### External Libraries 

To control the UR robot, the project relies on the `ur_rtde` library, which can be installed in your PC using `pip`. Follow these steps:

1. **Install ur_rtde Library:**
 Open your command-line interface (such as the terminal on Linux/Mac or Command Prompt on Windows) and enter the following command::

   ```bash
   pip install ur_rtde
   ```
   For detailed instructions on installing the library and checking OS-related requirements for your computer, refer to the documentation available in the official repository: https://gitlab.com/sdurobotics/ur_rtde

   
2. **Install Behave:**
   
To install Behave on your computer using `pip`, open your command-line interface and follow these simple steps.

```bash
pip install behave
```

Press "Enter" to execute the command. Pip will automatically download and install Behave and its dependencies. Once the installation is complete, you can verify it by checking the installed version:

```bash
behave --version
```

Now that the `ur_rtde` library and Behave have been successfully installed using `pip`, the IDE should locate any imports from these libraries. However, if you encounter issues finding file locations during execution, follow these steps:

- Open Eclipse and go to `Window -> Preferences -> PyDev -> Interpreters -> Python Interpreter -> Libraries`.
- Add the path of the `site-packages` directory associated with your Python installation. Including the path `site-packages` will ensure that the IDE can effectively identify and utilize the Behave and `ur_rtde` libraries.

### Code Execution  

1. **Environment Setup**
   - Go to `dk.sdu.bdd.xtext.examples/src/dk/sdu/bdd/xtext/examples/features/Environment.json` and open the "Environment.Json" file.
   - The "Environment.Json" file contains essential data and properties related to the robotic equipment and environment.
   - Customize the file with your specific data for your setup. Key data points to modify include the robot and gripper IP, robot positions for the pick-and-place task, as well as the digital inputs and outputs indexes chosen during their installation on the robot PLC.
  
2. **Scenario Definition**
   - Navigate to `/dk.sdu.bdd.xtext.examples/src/dk/sdu/bdd/xtext/examples` to locate the `sample.bdd` file.
   - Create your own scenario adhering to the DSL's grammar rules. The grammar rules are outlined in the "BddDsl.xtext" file, accessible under `/dk.sdu.bdd.text/src/dk/sdu/bdd/xtext/`. When writting your scenario, ensure compliance with the keywords defined in the "Environment.Json" file to identify entities, their states, and other properties.

3. **Scenario Execution**
   - Go to `/dk.sdu.bdd.xtext.examples/src/dk/sdu/bdd/xtext/examples/features`.
   - Open the 'main.py' file and execute it.
  
### Implementing New Grammar Rules

If you wish to modify the DSL and establish your own language and grammar rules, follow these steps:

1. **Implementing a New DSL:**
   - Navigate to `/dk.sdu.bdd.text/src/dk/sdu/bdd/xtext/` and make changes to the "BddDsl.xtext" file.
   - For assistance in implementing a new DSL, refer to this tutorial: [Xtext Domain Model Walkthrough](https://eclipse.dev/Xtext/documentation/102_domainmodelwalkthrough.html).

2. **Generate Xtext Artifacts:**
   - After defining your grammar rules, right-click on the "GenerateBddDsl.mwe2" file located under `/dk.sdu.bdd.text/src/dk/sdu/bdd/xtext/` and select `Run As -> MWE2 Workflow`.

3. **Run Eclipse Application:**
   - Right-click on the project and choose `Run As -> Eclipse Application`.
   - This action launches a runtime Eclipse instance equipped with the DSL editor.

4. **Create a New DSL File:**
   - Within the runtime Eclipse instance, create a new general project through the menu navigation.
   - Inside the new project, generate a new file using the designated extension defined during DSL creation. You should observe the successful integration of your DSL, as Xtext automatically generates features such as syntax highlighting, code completion, error checking, and content assist.

###  Code Structure and Package Explorer Navigation Guide

1. **DSL Code Location:**
- The code related to the DSL is situated under the project at  `/dk.sdu.bdd.text/src/dk/sdu/bdd/xtext/`.
- The key file is "BddDsl.xtext" which, as depicted in the image below, defines Xtext grammar rules for the DSL.

![image](https://github.com/Anahide-Vanian/DSL4Students/assets/72527140/bdfb49a0-e128-45a5-871a-f80ba5c08663)

2. **End-User Interaction:**

- Under `/dk.sdu.bdd.xtext.examples/src/dk/sdu/bdd/xtext/examples`, two ".bdd" extension files are present. They constitute the only files which end-users should use.
- "sample.bdd" include declarative entities and the scenario written in natural language for robotic setup execution.
- "robotic_domain.bdd" is utilized for imperative entity declarations.
They are the only files that the end-users has to deal with. The "sample.bdd" file contains the definition of all the declarative entities followed with the case scenario to run on the robotic setup (see picture below). 

![image](https://github.com/Anahide-Vanian/DSL4Students/assets/72527140/ea8ed85f-4816-4fa9-b57d-bb56ab826386)

3. **Execution Code:**

- The  execution code is within the `/dk.sdu.bdd.xtext.examples` project.
- Upon launching the main file, depicted below, the readFile() method processes the user-written "sample.bdd" file to generate a feature file. 

![image](https://github.com/Anahide-Vanian/DSL4Students/assets/72527140/579bc5cc-a81a-4daf-88b1-b6d08767a3fd)

4. **Feature File Generation:**

- Inside the directory `/dk.sdu.bdd.xtext.examples/src/dk/sdu/bdd/xtext/examples/features/logic`, you will find a file named "fileReader.py" (shown below). This file defines the readFile() method, responsible for transforming user scenarios into a feature file using the Gherkin syntax.
  
  ![image](https://github.com/Anahide-Vanian/DSL4Students/assets/72527140/87bf5408-ccb5-42e9-aebd-edb78492140c)

  Feature files describe the behavior of the application, but they are written in a special human-readable language called Gherkin. This specific language is essential because it allows Behave, a tool introduced later, to create executable code based on the user's descriptions.
  
- The generated feature file , named "tests.feature" is saved under `/dk.sdu.bdd.xtext.examples/src/dk/sdu/bdd/xtext/examples/features`.
  
![image](https://github.com/Anahide-Vanian/DSL4Students/assets/72527140/c70ac03e-5d14-46a3-8402-3a8b7849527e)


5.**Behave Framework Integration:**

- The main function initiates the execution of "behave_main()".

- Upon launching "behave_main()", Behave interprets the feature file "tests.feature" and matches each requested Gherkin step with corresponding step definitions (functions written in Python).

- The "tests.py" file, found at `/dk.sdu.bdd.xtext.examples/src/dk/sdu/bdd/xtext/examples/features/steps`, is where Behave looks for these step definitions, linking our story to a list of executable python commands.

![image](https://github.com/Anahide-Vanian/DSL4Students/assets/72527140/4d7c83bd-f2d2-4f18-8fb5-1993c1660916)

- Effective communication and execution of actions on the UR robot require specialized methods from the ur_rtde library. These methods are defined in the "environment.py" file, situated at `/dk.sdu.bdd.xtext.examples/src/dk/sdu/bdd/xtext/examples/features`. The "environment.py" file contains additional functions defining how the robot should perform tasks and interacts with the ur_rtde library.

6. **Robot Gripper Interaction:**

In `/dk.sdu.bdd.xtext.examples/src/dk/sdu/bdd/xtext/examples/features/logic/sdu_robotics`, two Python files contain methods for communicating with the robot gripper.
These files are utilized by "environment.py" for robot interaction.



### Note:
- Ensure that all necessary dependencies and plugins are installed in Eclipse for proper DSL development.
- Refer to the project documentation for detailed information on DSL syntax rules and usage.
