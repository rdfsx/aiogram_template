db.createUser(
        {
            user: "$MONGODB_USERNAME",
            pwd: "$MONGODB_PASSWORD",
            roles: [
                {
                    role: "readWrite",
                    db: "$MONGODB_DATABASE"
                }
            ]
        }
);