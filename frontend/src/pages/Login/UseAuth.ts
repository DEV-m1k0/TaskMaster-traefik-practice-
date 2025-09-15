import type { LoginUser, Token } from "./Interfaces"
import { authService } from "./AuthService"
import { useState } from "react"

export const useAuth = () => {
    const [token, setToken] = useState<string | null>(localStorage.getItem("access_token"))

    const login = async (credentials: LoginUser) => {
        try {
            const data: Token = await authService.login(credentials);
            setToken(data.access_token)
            localStorage.setItem("access_token", data.access_token)
            console.log(data)
        } catch {
            throw new Error("Login failed")
        }
    }
    

    const logout = () => {
        setToken(null)
        localStorage.removeItem('access_token')
    }

    return {login, logout, token}
}