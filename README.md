# Eye Drowsiness Detection Project

This project aims to develop a system for detecting drowsiness in drivers using machine learning techniques. It consists of three main modules: the machine learning (ML) module, the frontend module, and the backend module.

#### Note Replace supabase fields in db/db.py
### Running the Frontend Module

To run the frontend module, follow these steps:

1. Open a terminal and navigate to the frontend module directory: `cd frontend`.
2. Install the required dependencies by running: `npm install`.
3. Start the development server by running: `npm run dev`.
4. The frontend module should now be running, and you can access it by opening the provided URL in a web browser.

### Running the Backend Module

To run the backend module, follow these steps:

1. Open a terminal and navigate to the backend module directory.
2. Run the main Python file using the command: `python main.py`.
3. The backend module should now be running.
## Machine Learning Module

The ML module focuses on implementing eye detection techniques, collecting training data, selecting and training ML models, and evaluating the performance of the drowsiness prediction system. The module employs computer vision algorithms to detect eyes in images or video frames, extract relevant features, and feed them into ML models for drowsiness prediction. Various ML models can be experimented with, such as convolutional neural networks (CNNs), support vector machines (SVMs), or recurrent neural networks (RNNs). The module also defines evaluation metrics to assess the accuracy and efficiency of the trained models.

## Frontend Module

The frontend module is built using React, a JavaScript library for building user interfaces. It encompasses the design and development of the user interface (UI) for the drowsiness detection system. The frontend module includes real-time data display components that show the status of the driver's alertness, analytics components to present performance metrics, a driver blocking functionality to prevent driving while drowsy, and user authentication to ensure secure access to the system. The UI provides an intuitive and user-friendly experience for monitoring and interacting with the drowsiness detection system.

## Backend Module

The backend module is responsible for managing data synchronization and storage. It utilizes Supabase, a real-time database platform, to store and synchronize data across different devices and users. The module incorporates APIs provided by Supabase to handle data retrieval and modification operations. The backend module stores various types of data related to the drowsiness detection system, including trip data, performance metrics, and images collected during trips. The Supabase database provides a scalable and reliable solution for data management, enabling efficient storage and retrieval of information.

## Integration

The project integrates the machine learning module with the frontend module, enabling real-time drowsiness detection and display of results in the UI. The ML module's trained models are employed to analyze eye data captured by the system, and the frontend module receives the predictions and displays them to the user. The integration ensures smooth coordination between the ML algorithms and the user interface, providing accurate and timely feedback on driver alertness.

## Installation and Setup

To set up the project locally, follow these steps:

1. Clone the project repository from [GitHub Repository URL].
2. Install the required dependencies for the ML module, frontend module, and backend module.
3. Configure the ML module by setting up the required libraries, datasets, and training procedures.
4. Set up the frontend module by configuring the React environment, installing dependencies, and linking it to the ML module.
5. Configure the backend module by setting up a Supabase account, creating a new project, and obtaining the necessary API keys.
6. Update the configuration files of the frontend and backend modules with the appropriate API keys and connection details.
7. Start the ML module, frontend module, and backend module, and ensure they are running without errors.



## How to Use

Once the ML module, frontend module, and backend module are running, follow these steps to use the drowsiness detection system:

1. Access the frontend module by opening the provided URL in a web browser.
2. Authenticate yourself using the provided user authentication functionality.
3. The system will start capturing eye data and analyzing it for drowsiness.
4. The UI will display real-time data, such as the driver's alertness status and performance metrics.
5. If the system detects drowsiness, it may activate the driver blocking functionality to prevent further driving.
6. Monitor the system's feedback and take appropriate action to ensure driver safety.

## Contributing

We welcome contributions to enhance the functionality and performance of the drowsiness detection system. If you would like to contribute, please follow these guidelines:

1. Fork the project repository and create a new branch for your contribution.
2. Make the necessary changes, following the project's coding style and guidelines.
3. Write tests to ensure the correctness of your modifications.
4. Submit a pull request with a detailed description of the changes and their purpose.
5. Engage in the review process, addressing any feedback or questions.

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute the codebase for both commercial and non-commercial purposes.

## Contact

If you have any questions, suggestions, or feedback regarding the project, please contact [Project Contact Email]. We appreciate your interest and support in improving the drowsiness detection system.
