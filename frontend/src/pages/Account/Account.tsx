import { useEffect, useState } from "react";
import { useAuth } from "../Login/UseAuth"
import { authService } from "../Login/AuthService";
import type { User } from "../Login/Interfaces";

function AccountPage() {
    const { token } = useAuth();
    const [user, setUser] = useState<User>()

    useEffect(() => {
        const fetchData = async () => {
            if (token) {
                try {
                    const response: User = await authService.get_profile_data(token)
                    console.log(response)
                    setUser(response)
                } catch {
                    throw new Error("Failed to get account data")
                }
            }
        }
        fetchData()
    }, [token])

    return (
        <>
            <h1>Account Page</h1>
            <p>{user?.username ? user.username : "loading..."}</p>
        </>
    )
}

export default AccountPage