import axios from "axios";
import type { LoginUser } from "./Interfaces";


export const authService = {
    async login(credentials: LoginUser) {
        try {
            const response = await axios.post('/api/auth/login', {
                "username": credentials.username,
                "password": credentials.password
            })
            if (response.status != 200) {
                throw new Error("Login failed")
            }
            return response.data

        } catch (error) {
            console.error('Error during login:', error)
        }
    },

    async get_profile_data(token: string) {
        try {
            const response = await axios.get("/api/auth/account", {
                headers: {
                    Authorization: `Bearer ${token}`
                }
            })

            if (response.status != 200) {
                throw new Error("Authorization failed")
            }

            return response.data
        } catch {
            throw new Error("Authorization failed")
        }
    }
}