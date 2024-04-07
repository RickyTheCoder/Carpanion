import React from 'react';
import { View, Text, Button } from 'react-native';
import ButtonComponent from '../components/button';
import { H1 } from '../components/typography';
import InputComponent, { PasswordInputComponent } from '../components/input';

import { Input } from '@rneui/themed';

import {SecureStore} from 'expo';
import { useAuth } from '../components/AuthProvider';
import { useNavigation } from '@react-navigation/native';

export default function RegisterScreen ()
{
  const [email, setEmail] = React.useState("");
  const [password, setPassword] = React.useState("");
  const [confirmPassword, setConfirmPassword] = React.useState("");
 const { setToken } = useAuth();
  const navigation = useNavigation();

  const register = async () => {
    const res = await fetch('http://10.103.232.163:8000/api/v1/auth/registration/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ email, password1: password, password2: confirmPassword }),
    })
    
    const data = await res.json()

    console.log(res.ok)

    if (res.ok) {
      setToken(data.key)
      navigation.navigate('Video Feed')
      
    } else {
      //console.log(res.headers)
    }
  }
    return (
        <View style={{ backgroundColor: 'white', flex: 1, justifyContent: 'center', alignItems: 'center', gap: '100', 'padding': 28, marginTop: '', 'height': '100%' }}>
          <View style={{ alignItems: 'center', width: '100%', 'gap': '16' }} >
            <H1 text="Register" />
            <Input placeholder={'Email'} onChangeText={(text) => setEmail(text)} />
            <Input secureTextEntry placeholder={'Password'} onChangeText={(text) => setPassword(text)} />
            <Input secureTextEntry placeholder={'Confirm Password'} onChangeText={(text) => setConfirmPassword(text)} />

            <Button title='Login' onPress={() => navigation.navigate('Login')} color='#46A4D9' />
          </View>

          <View style={{ alignItems: 'center', width: '100%', 'gap': '8' }} >
            <ButtonComponent title="Register" onPress={register} />
          </View>
         
        </View>
      );
}