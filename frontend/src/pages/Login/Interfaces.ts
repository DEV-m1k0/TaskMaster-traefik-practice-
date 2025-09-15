interface LoginUser {
    username: string
    password: string
}

interface Token {
    access_token: string
    token_type: string
}

interface User {
    username: string
    password: string
}

export type { LoginUser, Token, User }