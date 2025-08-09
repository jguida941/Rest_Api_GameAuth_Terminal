# GameAuth Security Documentation

## Authorization Matrix

This document outlines the security permissions for each role in the GameAuth system.

### User Roles

1. **ADMIN** - Full system access
2. **USER** - Standard user access  
3. **PLAYER** - Limited read-only access (future game features)
4. **GUEST** - Minimal access (authentication check only)

### API Endpoint Permissions

| Endpoint | Method | ADMIN | USER | PLAYER | GUEST | Description |
|----------|--------|-------|------|--------|-------|-------------|
| `/gameusers` | GET | ✅ | ✅ | ✅ | ✅ | List all users |
| `/gameusers/{id}` | GET | ✅ | ✅ | ❌ | ❌ | Get specific user |
| `/gameusers` | POST | ✅ | ❌ | ❌ | ❌ | Create new user |
| `/gameusers/{id}` | PUT | ✅ | ✅ | ❌ | ❌ | Update user |
| `/gameusers/{id}` | DELETE | ✅ | ❌ | ❌ | ❌ | Delete user |
| `/status` | GET | ✅ | ✅ | ✅ | ✅ | API status check |
| `/healthcheck` | GET | ✅ | ✅ | ✅ | ✅ | Health monitoring |

### Expected Behavior

#### For GUEST and PLAYER roles:
- Can successfully access `/gameusers` and see the full user list
- Attempting to access `/gameusers/{id}` returns:
  ```json
  {"code":403,"message":"User not authorized."}
  ```

#### For USER role:
- Can view all users and individual user details
- Can update user information
- Cannot create or delete users

#### For ADMIN role:
- Full access to all endpoints
- Can perform all CRUD operations

## Security Implementation Details

### Authentication
- **Current**: HTTP Basic Authentication
- **Future**: JWT tokens with OAuth2 support

### Authorization 
- Implemented using Dropwizard's `@RolesAllowed` annotation
- `GameAuthorizer` class validates user roles
- Each endpoint explicitly declares required roles

### Password Security
- **Current**: Plaintext (demo only) 
- **Future**: bcrypt hashing with salt

## Common Security Issues

### Issue: GUEST/PLAYER can see user data
**Fix Applied**: Changed `@PermitAll` to `@RolesAllowed({"USER", "ADMIN"})` on user endpoints

### Issue: Missing authorization on PUT/DELETE
**Fix Applied**: Added proper `@RolesAllowed` annotations to all modifying endpoints

## Testing Authorization

### Test with cURL:
```bash
# GUEST access (should fail with 403)
curl -u guest:password http://localhost:8080/gameusers

# USER access (should succeed)
curl -u user:password http://localhost:8080/gameusers

# ADMIN delete (should succeed)
curl -X DELETE -u admin:password http://localhost:8080/gameusers/1
```

### Test Matrix:
1. **GUEST** → `/gameusers` → 403 Forbidden 
2. **GUEST** → `/gameusers/1` → 403 Forbidden 
3. **PLAYER** → `/gameusers` → 403 Forbidden 
4. **PLAYER** → `/gameusers/1` → 403 Forbidden 
5. **USER** → `/gameusers` → 200 OK 
6. **USER** → `/gameusers/1` → 200 OK 
7. **USER** → DELETE `/gameusers/1` → 403 Forbidden 
8. **ADMIN** → All endpoints → 200 OK 

## Future Security Enhancements

1. **JWT Implementation**
   - Stateless authentication
   - Token expiration
   - Refresh tokens

2. **Rate Limiting**
   - Per-user request limits
   - IP-based throttling
   - DDoS protection

3. **Audit Logging**
   - Track all authentication attempts
   - Log authorization failures
   - Monitor suspicious patterns

4. **Enhanced RBAC**
   - Fine-grained permissions
   - Dynamic role assignment
   - Permission inheritance

---

**Last Updated**: July 2025

**Security Contact**: justin.guida@snhu.edu
