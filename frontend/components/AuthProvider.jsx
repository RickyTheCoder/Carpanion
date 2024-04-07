import { useContext, createContext, useState, useEffect } from 'react';
import {SecureStore} from 'expo';

const AuthContext = createContext({
    token: null,
    setToken: () => {},
    isAuthenticated: () => {},
    getToken: () => {},
});

export const useAuth = () => useContext(AuthContext);

export function AuthProvider({ children }) {
    const [token, setToken] = useState(null);

    const isAuthenticated = () => {
        return token !== null;
    }

    const getToken = () => {
        return token;
    }

    const setTokenC = (token) => {
        setToken(token);
        SecureStore.setItemAsync('token', token);
    }

    useEffect(() => {
        const getToken = async () => {
            const token = await SecureStore.getItemAsync('token');
            if (token) {
                setToken(token);
            }
        }

        getToken();
    }, []);



    return (
        <AuthContext.Provider value={{ token, setToken: setTokenC, isAuthenticated, getToken }}>
            {children}
        </AuthContext.Provider>
    )
}