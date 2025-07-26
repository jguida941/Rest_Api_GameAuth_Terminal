# GameAuth Project Context & Memory

## Project Overview
GameAuth is a REST API authentication service built with Dropwizard that's being evolved into a comprehensive gaming platform. The project features a distinctive neon-themed terminal UI and is designed to scale from basic authentication to a full multiplayer gaming infrastructure.

## Current Implementation Details

### Terminal UI Design
- **Color Scheme**: Neon orange/red cyberpunk aesthetic
- **Key Achievement**: Fixed terminal alignment issues by properly handling ANSI escape codes
- **Helper Functions**: 
  - `visible_length()`: Calculates text length excluding ANSI codes
  - `print_box_line()`: Ensures consistent box width
  - Unit tests verify alignment

### Authentication System
- **Current**: HTTP Basic Auth with 4 roles (Admin, User, Player, Guest)
- **Users**: Stored in-memory with hardcoded credentials
- **Endpoints**: `/gameusers`, `/status`, `/healthcheck`

### Technical Stack
- Java 8 with Dropwizard 2.0.18
- Maven build system
- Python launcher script with custom UI
- In-memory database (transitioning to PostgreSQL)

## Key Design Decisions

1. **Terminal UI Over Web UI**: Chose to create an engaging terminal experience for developers
2. **Dropwizard Over Spring**: Lighter weight, perfect for microservices evolution
3. **Python Launcher**: Better cross-platform support and visual appeal
4. **Role-Based Access**: Prepared for game-specific permissions

## Future Vision & Roadmap

### Phase 1: Security Enhancement
- JWT tokens replacing Basic Auth
- OAuth2 integration (Discord, Steam, Twitch)
- 2FA implementation
- bcrypt password hashing

### Phase 2: Real-Time Gaming
- WebSocket support for live updates
- Game room management
- Matchmaking with ELO/MMR
- Anti-cheat systems

### Phase 3: Platform Features
- Player profiles and statistics
- Leaderboards and rankings
- In-game economy
- Social features (friends, guilds, chat)

### Phase 4: Modern Frontend
- React/Vue dashboard
- Mobile applications
- Developer portal with API playground
- Game engine SDKs

### Phase 5: Infrastructure
- Microservices architecture
- PostgreSQL + Redis + MongoDB
- Kubernetes deployment
- Prometheus/Grafana monitoring

## Code Patterns & Standards

### Java Code Style
- Use existing patterns from the codebase
- Prefer composition over inheritance
- Follow Dropwizard conventions
- Comprehensive JavaDoc comments

### Python Scripts
- ANSI escape codes for colors
- Consistent box drawing functions
- Error handling for cross-platform compatibility
- Clear commenting for maintenance

### Testing Approach
- Unit tests for critical functions
- Integration tests for API endpoints
- Performance tests for scalability
- Visual tests for UI components

## Common Tasks & Commands

### Building & Running
```bash
mvn clean package
python3 run_server.py
# or double-click START_SERVER.command
```

### Testing
```bash
mvn test
python3 test_alignment.py
```

### Git Workflow
```bash
git add .
git commit -m "descriptive message"
git push origin master
```

## Problem Solutions

### Terminal Alignment Issues
- Problem: ANSI codes counted in string length
- Solution: Strip codes before calculating padding
- Test: `test_alignment.py` verifies all borders align

### Port Already in Use
- Check: `lsof -i :8080`
- Kill: `kill -9 <PID>`
- Alternative: Change port in config.yml

## Project Philosophy

This project emphasizes:
1. **Developer Experience**: Beautiful, functional terminal UI
2. **Scalability**: Architecture ready for millions of players
3. **Security First**: Modern authentication practices
4. **Real-Time Performance**: Low-latency game state synchronization
5. **Community Driven**: Open source with clear contribution guidelines

## Next Implementation Priorities

1. **Database Migration**: Move from in-memory to PostgreSQL
2. **JWT Authentication**: Implement stateless auth tokens
3. **WebSocket PoC**: Create simple real-time demo
4. **CI/CD Pipeline**: Automate testing and deployment
5. **API Documentation**: OpenAPI/Swagger integration

## Notes for Future Development

- The terminal UI is a key differentiator - maintain its quality
- Consider backward compatibility when adding features
- Performance metrics should drive architectural decisions
- Security audits before each major release
- Community feedback shapes the roadmap

---

Last Updated: July 2025
Project Repository: https://github.com/jguida941/Rest_Api_GameAuth_Terminal