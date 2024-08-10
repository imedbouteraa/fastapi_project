
# FastAPI OCR API

This project is a FastAPI-based application that provides Optical Character Recognition (OCR) functionality for processing images of Driver's Licenses, Carte Grises, and ID Cards. The application exposes three API endpoints that can be used to upload images and extract relevant information.

## Table of Contents

- [Project Structure](#project-structure)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [API Endpoints](#api-endpoints)
- [Integrating with a Mobile App](#integrating-with-a-mobile-app)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

```
.
├── media/
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   ├── driver_license.js
│   │   ├── carte_crise.js
│   │   └── idcard.js
│   └── img/
│       └── loading-spinner.gif
├── templates/
│   ├── index.html
│   ├── driver_license.html
│   ├── carte_crise.html
│   └── idcard.html
├── venv/
├── Dockerfile
├── main.py
├── README.md
├── requirements.txt
├── serializers.py
└── views.py
```

## Features

- **OCR for Driver's License**: Extracts information such as name, date of birth, license number, etc.
- **OCR for Carte Grise**: Extracts vehicle information including registration number, VIN, and more.
- **OCR for ID Card**: Extracts personal information like name, nationality, ID number, etc.
- **User Interface**: A basic web interface using HTML, CSS, and JavaScript to interact with the API.
- **Docker Support**: Deployable via Docker for consistent environments.

## Installation

### Prerequisites

- **Python 3.9+**
- **pip**
- **Git**

### Clone the Repository

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Running the Application Locally

```bash
uvicorn main:app --reload
```

- Access the application in your browser at `http://127.0.0.1:8000`.
- Navigate to the different OCR pages to test the OCR functionality.

### Using Docker

1. **Build the Docker Image**:

   ```bash
   docker build -t fastapi-ocr .
   ```

2. **Run the Docker Container**:

   ```bash
   docker run -d -p 8000:8000 fastapi-ocr
   ```

- Access the application at `http://localhost:8000`.

## Deployment

### Deploying on Render

1. **Connect Your Repository**: Link your GitHub repository to Render.
2. **Configure the Service**:
   - Set the build command to `pip install -r requirements.txt`.
   - Set the start command to `uvicorn main:app --host 0.0.0.0 --port $PORT`.
3. **Deploy**: Render will automatically build and deploy your application.

### Deploying on Heroku

1. **Create a Heroku App**:
   ```bash
   heroku create your-app-name
   ```
2. **Push to Heroku**:
   ```bash
   git push heroku master
   ```
3. **Access Your Application**: Heroku will provide a public URL.

## API Endpoints

### 1. **Driver License OCR**
   - **Endpoint**: `/api/ocr/driver_license/`
   - **Method**: `POST`
   - **Request Body**: `image` (file)
   - **Response**: JSON with extracted information.

### 2. **Carte Grise OCR**
   - **Endpoint**: `/api/ocr/carte_crise/`
   - **Method**: `POST`
   - **Request Body**: `image` (file)
   - **Response**: JSON with extracted information.

### 3. **ID Card OCR**
   - **Endpoint**: `/api/ocr/idcard/`
   - **Method**: `POST`
   - **Request Body**: `image` (file)
   - **Response**: JSON with extracted information.

## Integrating with a Mobile App

You can integrate this API with any mobile app by making HTTP POST requests to the respective endpoints. Convert the images to base64 and send them in the request body.

### Example with Flutter:

```dart
import 'package:http/http.dart' as http;
import 'dart:convert';

Future<void> fetchDriverLicenseData() async {
  final response = await http.post(
    Uri.parse('https://your-app-name.onrender.com/api/ocr/driver_license/'),
    headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',
    },
    body: jsonEncode(<String, String>{
      'image': base64Encode(yourImageBytes), // Convert image to base64 string
    }),
  );

  if (response.statusCode == 200) {
    final Map<String, dynamic> data = jsonDecode(response.body);
    print(data);
  } else {
    throw Exception('Failed to load data');
  }
}
```

## Contributing

Contributions are welcome! Please create an issue or a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.




Happy coding!


