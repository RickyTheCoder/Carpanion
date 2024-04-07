import React from 'react';
import { View, Text, Button } from 'react-native';
import ButtonComponent from '../components/button';
import { H1 } from '../components/typography';
import InputComponent, { PasswordInputComponent } from '../components/input';

import {SecureStore} from 'expo';
import { useAuth } from '../components/AuthProvider';

export default function LoginScreen ()
{
  const [email, setEmail] = React.useState("");
  const [password, setPassword] = React.useState("");
  const [loading, setLoading] = React.useState(false);
 const { isAuthenticated, setToken } = useAuth();

  const login = async () => {
    const res = await fetch('http://10.103.232.163:8000/api/v1/auth/login/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ email, password }),
    })
    
    const data = await res.json()

    if (res.status === 200) {
      setToken(data.token)
    } else {
      console.log(res.headers)
    }
  }
    return (
        <View style={{ backgroundColor: 'white', flex: 1, justifyContent: 'center', alignItems: 'center', gap: '100', 'padding': 28, marginTop: '', 'height': '100%' }}>
          <View style={{ alignItems: 'center', width: '100%', 'gap': '16' }} >
            <H1 text="Login" />
            <InputComponent placeholder="Email" value="" onChangeText={(text) => setEmail(text)} />
            <PasswordInputComponent placeholder="Password" value="" onChangeText={(text) => setPassword(text)} />
          </View>

          <View style={{ alignItems: 'center', width: '100%', 'gap': '8' }} >
            <ButtonComponent title="Login" onPress={login} />
            <Button title="Forgot Password?" color={'#46A4D9'} onPress={() => console.log("Forgot Password button pressed")} />
          </View>
         
        </View>
      );
}