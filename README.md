# GameAuth REST API
![Java](https://img.shields.io/badge/Java-8+-orange.svg)
![Dropwizard](https://img.shields.io/badge/Dropwizard-2.0.18-blue.svg)
![Maven](https://img.shields.io/badge/Maven-3.6+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
<br>
**This is one of many versions I built of GameAuth a Rest API!**





**A secure, scalable REST API for game authentication and user management**




## Overview

GameAuth is a production-ready REST API built with Dropwizard framework, designed to handle authentication and user management for gaming applications. The project emphasizes security, scalability, and developer experience through a beautifully crafted terminal UI and straightforward deployment process.

### Why GameAuth?

- **Secure by Design**: Role-based access control with HTTP Basic Authentication
- **High Performance**: Built on Dropwizard's proven architecture
- **Beautiful Terminal UI**: Custom-designed neon-themed interface for enhanced developer experience
- **Easy Deployment**: One-click startup with automatic browser launch
- **Developer Friendly**: Clear documentation, intuitive API design, and helpful error messages

## Features

### Core Functionality
- **Multi-tier User Authentication**: Admin, User, Player, and Guest roles
- **RESTful API Design**: Clean, intuitive endpoints following REST best practices
- **Health Monitoring**: Built-in health check system for production monitoring
- **Automatic Configuration**: Zero-config startup with sensible defaults

### Developer Experience
- **One-Click Launch**: Double-click `START_SERVER.command` to start
- **Neon Terminal UI**: Cyberpunk-inspired interface with loading animations
- **Real-time Feedback**: Live server status and connection monitoring
- **Auto-Browser Launch**: Automatically opens the API in your default browser

## Quick Start

### Prerequisites
```bash
# Check Java version (8 or higher required)
java -version

# Check Maven version (3.6 or higher required)
mvn -version

# Check Python version (3.x required for launcher)
python3 --version
```

### Installation & Running

#### Option 1: One-Click Launch (Recommended)
```bash
# 1. Build the project
mvn clean package

# 2. Double-click START_SERVER.command in Finder
# That's it! Browser opens automatically
```

#### Option 2: Terminal Launch
```bash
# 1. Navigate to project
cd ~/Desktop/untitled\ folder\ 2/java-rest-api

# 2. Build the project
mvn clean package

# 3. Run with Python launcher
python3 run_server.py
```

### Login Credentials

| Role | Username | Password | Permissions |
|------|----------|----------|-------------|
| **Admin** | `admin` | `password` | Full CRUD access |
| **User** | `user` | `password` | Read, Update |
| **Player** | `player` | `password` | Read only |
| **Guest** | `guest` | `password` | Limited read |

## System Architecture

### High-Level Architecture Flow

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│                 │     │                  │     │                 │
│  Web Browser    │────▶│  GameAuth API    │────▶│  In-Memory DB   │
│  (Client)       │◀────│  (Dropwizard)    │◀────│  (User Store)   │
│                 │     │                  │     │                 │
└─────────────────┘     └──────────────────┘     └─────────────────┘
         │                        │                        │
         │                        ▼                        │
         │              ┌──────────────────┐               │
         └─────────────▶│  Auth Layer      │◀──────────────┘
                        │  (Basic Auth)    │
                        │                  │
                        └──────────────────┘
```

### Component Architecture

```
GameAuth Application
├── Presentation Layer
│   ├── REST Controllers (Jersey)
│   ├── JSON Serialization (Jackson)
│   └── HTTP Response Handling
│
├── Business Logic Layer
│   ├── Authentication Service
│   ├── Authorization Service
│   └── User Management Service
│
├── Data Access Layer
│   ├── In-Memory User Database
│   ├── DAO Pattern Implementation
│   └── Entity Models
│
└── Infrastructure Layer
    ├── Health Checks
    ├── Configuration Management
    └── Logging Framework
```

### Request Flow Diagram

```
Client Request
     │
     ▼
┌─────────────────────────────────────────────┐
│            HTTP Basic Auth Check             │
│  (Browser prompts for username/password)    │
└─────────────────────────────────────────────┘
     │ Credentials
     ▼
┌─────────────────────────────────────────────┐
│           GameAuthenticator                  │
│  - Validates credentials                     │
│  - Returns authenticated GameUser            │
└─────────────────────────────────────────────┘
     │ Valid User
     ▼
┌─────────────────────────────────────────────┐
│            GameAuthorizer                    │
│  - Checks user role permissions              │
│  - Grants/denies access to endpoint          │
└─────────────────────────────────────────────┘
     │ Authorized
     ▼
┌─────────────────────────────────────────────┐
│         REST Controller                      │
│  - Processes business logic                  │
│  - Returns JSON response                     │
└─────────────────────────────────────────────┘
```

## Design Choices

### 1. Dropwizard Framework
- **Why**: Production-ready, combines best-of-breed Java libraries
- **Benefits**: Built-in metrics, health checks, and configuration management
- **Alternative Considered**: Spring Boot (too heavyweight for this use case)

### 2. HTTP Basic Authentication
- **Why**: Simple, secure over HTTPS, browser-native support
- **Benefits**: No custom login page needed, works with all HTTP clients
- **Trade-off**: Less flexibility in UI customization

### 3. In-Memory Database
- **Why**: Simplicity for demo/development purposes
- **Benefits**: Zero configuration, fast performance, no external dependencies
- **Future**: Easy to swap with PostgreSQL/MySQL for production

### 4. Neon Terminal UI Design
- **Why**: Enhanced developer experience, clear visual feedback
- **Implementation**: ANSI escape codes for colors and animations
- **Benefits**: Makes server startup engaging and informative

### 5. Python Launcher Script
- **Why**: Cross-platform compatibility, better UX than raw Java commands
- **Features**: 
  - Auto-detects Java installation
  - Provides styled terminal output
  - Shows all login credentials upfront
  - Handles graceful shutdown

## API Documentation

### Base URLs
- **Main API**: `http://localhost:8080`
- **Health Check**: `http://localhost:8081`

### Endpoints

#### 1. List All Users
```http
GET /gameusers
Authorization: Basic <credentials>

Response: 200 OK
[
  {
    "id": 1,
    "username": "admin",
    "role": "ADMIN"
  },
  ...
]
```

#### 2. Get Specific User
```http
GET /gameusers/{id}
Authorization: Basic <credentials>

Response: 200 OK
{
  "id": 1,
  "username": "admin",
  "role": "ADMIN"
}
```

#### 3. Create New User (Admin only)
```http
POST /gameusers
Authorization: Basic <admin_credentials>
Content-Type: application/json

{
  "username": "newuser",
  "password": "securepass",
  "role": "USER"
}

Response: 201 Created
```

#### 4. Update User (Admin/User)
```http
PUT /gameusers/{id}
Authorization: Basic <credentials>
Content-Type: application/json

{
  "username": "updateduser",
  "role": "PLAYER"
}

Response: 200 OK
```

#### 5. Delete User (Admin only)
```http
DELETE /gameusers/{id}
Authorization: Basic <admin_credentials>

Response: 204 No Content
```

#### 6. Health Check
```http
GET /healthcheck

Response: 200 OK
{
  "status": "healthy",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

#### 7. API Status
```http
GET /status

Response: 200 OK
{
  "api": "GameAuth REST API",
  "version": "1.0.0",
  "status": "operational"
}
```

### Error Responses

```json
// 401 Unauthorized
{
  "code": 401,
  "message": "Invalid credentials"
}

// 403 Forbidden
{
  "code": 403,
  "message": "Insufficient permissions for this operation"
}

// 404 Not Found
{
  "code": 404,
  "message": "User not found"
}
```

## Terminal UI Design

### Design Philosophy
The terminal UI uses a cyberpunk/gaming aesthetic with neon colors to create an engaging developer experience.

### Color Palette
- **Primary**: Neon Orange (#FF6B35)
- **Secondary**: Bright Red (#FF0000)
- **Accent**: Yellow (#FFD700)
- **Success**: Bright Green (#00FF00)
- **Info**: Cyan (#00FFFF)

### UI Components

```
╔════════════════════════════════════════════════════════════╗
║                    Component Title                         ║
╠════════════════════════════════════════════════════════════╣
║  ▸ Bullet points with orange arrows                        ║
║  ▸ Consistent spacing and alignment                        ║
║  ▸ Red borders for visual hierarchy                        ║
╚════════════════════════════════════════════════════════════╝
```

### Loading Animation
```python
# Spinning progress indicator
loading_chars = ["◐", "◓", "◑", "◒"]

# Progress bar with percentage
[████████░░░░] 67% LOADING...
```

## Security

### Current Implementation
1. **HTTP Basic Authentication**: All endpoints require authentication
2. **Role-Based Access Control**: Different permissions per user type
3. **In-Memory User Store**: No persistent storage of credentials
4. **Password Handling**: Currently uses plaintext (for demo only)

### Production Recommendations
1. **Use HTTPS**: Enable SSL/TLS for encrypted communication
2. **Password Hashing**: Implement bcrypt or similar
3. **Token-Based Auth**: Consider JWT for stateless authentication
4. **Rate Limiting**: Prevent brute force attacks
5. **Audit Logging**: Track all authentication attempts

## Development

### Project Structure
```
java-rest-api/
├── src/
│   ├── main/
│   │   ├── java/com/gamingroom/gameauth/
│   │   │   ├── GameAuthApplication.java      # Main entry point
│   │   │   ├── GameAuthConfiguration.java    # Config POJO
│   │   │   ├── auth/                         # Authentication logic
│   │   │   │   ├── GameAuthenticator.java    # Validates credentials
│   │   │   │   ├── GameAuthorizer.java       # Checks permissions
│   │   │   │   └── GameUser.java             # User principal
│   │   │   ├── controller/                   # REST endpoints
│   │   │   │   └── GameUserRESTController.java
│   │   │   ├── dao/                          # Data access
│   │   │   │   └── GameUserDB.java           # In-memory database
│   │   │   ├── healthcheck/                  # Health monitoring
│   │   │   └── representations/              # DTOs
│   │   └── resources/
│   │       └── banner.txt                    # ASCII art banner
│   └── test/                                 # Unit tests
├── config.yml                                # Dropwizard config
├── pom.xml                                   # Maven config
├── run_server.py                             # Python launcher
└── START_SERVER.command                      # macOS launcher
```

### Building from Source
```bash
# Clean build
mvn clean package

# Run tests only
mvn test

# Skip tests
mvn package -DskipTests

# Generate documentation
mvn javadoc:javadoc
```

### Adding New Endpoints
1. Create new method in `GameUserRESTController`
2. Add appropriate `@Path` and HTTP method annotation
3. Implement authorization check if needed
4. Update this README with new endpoint documentation

### Modifying Terminal UI
Edit `run_server.py` to change:
- Colors: Modify ANSI escape codes
- Layout: Adjust print statements
- Animations: Change timing or characters

## Troubleshooting

### Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| **Port already in use** | `lsof -i :8080` then kill the process |
| **Java version error** | Install Java 8+ or update JAVA_HOME |
| **Maven build fails** | Run `mvn clean` then rebuild |
| **Permission denied on .command** | Right-click → Open → Allow |
| **Browser doesn't open** | Manually visit http://localhost:8080/gameusers |
| **Can't find JAR file** | Ensure `mvn package` completed successfully |

### Debug Mode
```bash
# Enable debug logging
java -jar target/gameauth-0.0.1-SNAPSHOT.jar server config.yml --debug

# Check server logs
tail -f server.log
```

### Health Check Monitoring
```bash
# Continuous health monitoring
watch -n 1 'curl -s http://localhost:8081/healthcheck | jq'
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.


## Support

For issues, questions, or contributions:
- Open an issue on GitHub
- Check existing documentation
- Review the troubleshooting guide
- This is one of many versions. I still need to double check everything.
- If you need help email me at justin.guida@snhu.edu
---

<div align="center">
Built with ❤️ using Dropwizard and Java
</div>
