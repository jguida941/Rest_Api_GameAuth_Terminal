# GameAuth REST API

A Dropwizard-based REST API for game authentication and user management.

## 🚀 Quick Start

1. **Build:** `mvn clean package`
2. **Run:** Double-click `START_SERVER.command`
3. **Login:** Username: `admin`, Password: `password`

## Prerequisites

- Java 8 or higher
- Maven 3.6 or higher
- Python 3 (for running the server easily)

## Running the Application - Easy Method

### 🚀 EASIEST WAY: Just Double-Click!

1. **Find the file:** `START_SERVER.command` 
2. **Double-click it**
3. **Your browser opens automatically with the login page!**

That's it! The terminal will show you all the login credentials and automatically open the login page in your browser.
(Tested on macOS)

### Alternative: Using run_server.py
1. **Find the file:** `run_server.py`
2. **Run in terminal:** `python3 run_server.py`
3. **Navigate to:** http://localhost:8080/gameusers

### 📋 Login Credentials

When the browser prompts for username/password, use:

| User Type | Username | Password | Access Level |
|-----------|----------|----------|--------------|
| Admin | `admin` | `password` | Full access (create, read, update, delete) |
| User | `user` | `password` | Read and update access |
| Player | `player` | `password` | Read access only |
| Guest | `guest` | `password` | Limited access |


### 🧪 Testing the API

After logging in, you'll see the user list. You can:

1. **View all users**: http://localhost:8080/gameusers (opens automatically)
2. **Check API status**: http://localhost:8080/status
3. **View specific user**: http://localhost:8080/gameusers/1

### 🛑 Stopping the Server

Press `Ctrl+C` in the terminal window to stop the server.

### Alternative Running Methods

**Python Script in VS Code:**
1. Open `run_server.py`
2. Click the Play button (▶️)

**Direct Java Command:**
```bash
java -jar target/gameauth-0.0.1-SNAPSHOT.jar server config.yml
```

## File Structure & Scripts

```
untitled folder 2/
└── java-rest-api/
    ├── START_SERVER.command   # 🚀 Double-click this to run!
    ├── run_server.py         # Python script that starts the server
    ├── config.yml            # Server configuration
    ├── pom.xml              # Maven build configuration
    ├── README.md            # This file
    ├── src/                 # Source code
    └── target/              # Built JAR files (created after building)
        └── gameauth-0.0.1-SNAPSHOT.jar
```

### How the Scripts Work

1. **START_SERVER.command** (Double-click to run)
   - This is a Python script disguised as a .command file
   - When you double-click it, macOS runs it automatically
   - It calls `run_server.py` and opens your browser

2. **run_server.py** (The actual server starter)
   - Simple Python script that runs the Java JAR
   - Can be run directly: `python3 run_server.py`
   - Used by START_SERVER.command

## API Endpoints

The application provides the following endpoints:

- **Health Check**: `GET http://localhost:8081/healthcheck`
- **User Authentication**: Available at `http://localhost:8080/api/`

## Configuration

The application uses `config.yml` for configuration. Currently configured settings:

- Logging level: INFO
- Gaming room package logging: DEBUG

## Building the Application

### Compiling the JAR File

**First time setup - Build the project:**
```bash
# Navigate to the project
cd ~/Desktop/untitled\ folder\ 2/java-rest-api

# Build the JAR file
mvn clean package
```

This creates: `target/gameauth-0.0.1-SNAPSHOT.jar`

### Running the Server - Two Easy Ways

**Method A: Double-Click (Easiest)**
- Find `START_SERVER.command` in Finder
- Double-click it
- Browser opens automatically!

**Method B: Using run_server.py**
```bash
# In terminal:
cd ~/Desktop/untitled\ folder\ 2/java-rest-api
python3 run_server.py
```

### Direct Java Command (If Scripts Don't Work)
```bash
cd ~/Desktop/untitled\ folder\ 2/java-rest-api
java -jar target/gameauth-0.0.1-SNAPSHOT.jar server config.yml
```

## Project Structure

```
java-rest-api/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── com/gamingroom/gameauth/
│   │   │       ├── GameAuthApplication.java      # Main application class
│   │   │       ├── GameAuthConfiguration.java    # Configuration class
│   │   │       ├── auth/                         # Authentication components
│   │   │       ├── controller/                   # REST controllers
│   │   │       ├── dao/                          # Database access
│   │   │       ├── healthcheck/                  # Health check components
│   │   │       └── representations/              # Data models
│   │   └── resources/
│   └── test/
├── config.yml                                    # Application configuration
├── pom.xml                                       # Maven configuration
├── START_SERVER.command                          # Double-click to run!
├── run_server.py                                 # Python script to start server
└── target/                                       # Build output directory
```

## Troubleshooting

### Common Issues

1. **"Command not found" errors**:
   - Make sure you have Python 3 installed: `python3 --version`
   - Make sure you have Java installed: `java -version`
   - Make sure you built the project: `mvn clean package`

2. **"Permission denied" when double-clicking START_SERVER.command**:
   - Right-click the file, select "Open"
   - macOS will ask if you're sure - click "Open"

3. **Port already in use**: If you get an error about port 8080 or 8081 being in use:
   - Find the process: `lsof -i :8080` or `netstat -an | grep 8080`
   - Stop the process or modify `config.yml` to use different ports

4. **Java version issues**: Ensure you're using Java 8 or higher:
   ```bash
   java -version
   ```

5. **JAR file not found**:
   - Build the project first: `mvn clean package`
   - Check the target directory: `ls -la target/`

6. **Build failures**: Try cleaning the project:
   ```bash
   mvn clean
   mvn package
   ```

## Development

To run in development mode with automatic reloading:

```bash
mvn compile exec:java
```

## Testing

Run the tests:
```bash
mvn test
```

## Additional Information

This application uses:
- Dropwizard 2.0.18 framework
- Jersey for REST endpoints
- Jackson for JSON processing
- Built-in authentication and authorization