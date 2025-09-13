import axios from "axios"
import { useState } from "react"

function Login() {

    const [formData, setFormData] = useState({
        username: '',
        password: ''
    })

    const handleInputChange = (e: { target: HTMLInputElement }) => {
        const { name, value } = e.target as HTMLInputElement
        setFormData({
            ...formData,
            [name]: value
        })
    }

    const btnOnClickHandler = async () => {
        const username = formData.username
        const password = formData.password

        try {
            const response = await axios.post('/api/auth/login', {
                "username": username,
                "password": password
            })
            console.log(response.data)
        } catch (error) {
            console.error('Error during login:', error)
        }
    }

    const checkHealth = async () => {
        try {
            const response = await axios.get('/api/auth/health')
            console.log(response.data)
        } catch (error) {
            console.error('Error checking health:', error)
        }
    }

    return (
        <>
            <h1>Login page</h1>
            <a href="/">Go to Index page</a>

            <button
                onClick={checkHealth}    
            >Check health</button>

            <div>
                <input
                    type="text"
                    placeholder="username"
                    onChange={handleInputChange}
                    name="username"
                />
                <input 
                    type="password"
                    placeholder="password"
                    onChange={handleInputChange}
                    name="password" 
                />
                <button onClick={btnOnClickHandler}>Login</button>
            </div>
        </>
    )
}

export default Login