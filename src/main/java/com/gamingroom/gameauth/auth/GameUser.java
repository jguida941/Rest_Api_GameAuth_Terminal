package com.gamingroom.gameauth.auth;

import java.security.Principal;
import java.util.Set;

/**
 * GameUser - Represents an authenticated user in the system.
 * 
 * This class implements Principal from Java Security API, making it compatible
 * with Dropwizard's authentication framework. Each user has a name and optional roles.
 */
public class GameUser implements Principal {
    // User's login name (e.g., "guest", "user", "player", "admin")
    private String name = "";
 
    // Set of roles assigned to this user (e.g., "USER", "ADMIN")
    // Using Set<String> allows users to have multiple roles
    private final Set<String> roles;
 
    /**
     * Constructor for users without roles (like guest users).
     * @param name The username
     */
    public GameUser(String name) {
        this.name = name;
        this.roles = null;
    }
 
    /**
     * Constructor for users with roles.
     * @param name The username
     * @param roles Set of role strings (e.g., ImmutableSet.of("USER", "ADMIN"))
     */
    public GameUser(String name, Set<String> roles) {
        this.name = name;
        this.roles = roles;
    }
 
    /**
     * Required by Principal interface.
     * @return The username
     */
    public String getName() {
        return name;
    }
 
    /**
     * Generates a random ID for the user.
     * Note: In production, this should use a persistent ID from a database.
     * @return A random integer ID
     */
    public int getId() {
        return (int) (Math.random() * 100);
    }
 
    /**
     * Gets the user's roles. Used by GameAuthorizer to check permissions.
     * 
     * IMPORTANT: This method is getRoles() (plural), not getRole() (singular).
     * This allows users to have multiple roles (e.g., admin has both "ADMIN" and "USER").
     * 
     * @return Set of role strings, or null if user has no roles (like guest)
     */
    public Set<String> getRoles() {
        return roles;
    }
}