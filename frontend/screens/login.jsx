import { View, Text } from 'react-native';
import ButtonComponent from '../components/button';

export default function LoginScreen ()
{
    return (
        <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
          <Text>Login!</Text>
          <ButtonComponent title="Login" onPress={() => console.log("Login button pressed")} />
        </View>
      );
}