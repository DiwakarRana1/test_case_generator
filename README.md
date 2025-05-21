# Test Case Generator

A web application that automatically generates test cases using Google's Gemini AI model. The application can generate test cases from various inputs including feature descriptions, code snippets, user stories, API specifications, PDFs, JIRA tickets, and application URLs.

## Features

- Web-based interface for easy interaction
- AI-powered test case generation
- Support for multiple input types
- Structured test case output format
- Real-time response streaming

## Project Structure

```
.
├── app.py                 # Main Flask application
├── test_case_generator.py # Core test case generation logic
├── requirements.txt       # Project dependencies
├── templates/            # HTML templates
│   └── index.html       # Main web interface
├── venv/                # Python virtual environment
└── README.md           # Project documentation
```

## Prerequisites

- Python 3.7 or higher
- Google Cloud Platform account with Vertex AI API enabled
- Google Cloud project with Gemini API access

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Test_Case_generation
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up Google Cloud credentials:
   - Create a service account in Google Cloud Console
   - Download the service account key JSON file
   - Set the environment variable:
     ```bash
     export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service-account-key.json"
     ```

## Running the Application

1. Start the Flask development server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

## Usage

1. Enter your input in the web interface. This can be:
   - Feature descriptions
   - Code snippets
   - User stories
   - API specifications
   - PDFs
   - JIRA tickets
   - Application URLs

2. Click the generate button to create test cases

3. The generated test cases will follow this format:
   - Test Case Title
   - Description
   - Preconditions
   - Test Steps
   - Expected Result
   - Test Type (Unit, Functional, Integration, Edge, etc.)

## API Endpoints

- `GET /`: Serves the main web interface
- `POST /generate`: Accepts JSON input with a 'prompt' field and returns generated test cases

## Dependencies

- Flask 2.0.1
- Werkzeug 2.0.3
- google-generativeai 0.3.2

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

