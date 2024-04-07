import * as React from 'react';
import { Text, View } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import LoginScreen from './screens/login';
import MessageLog from './screens/messagelog';
import Settings from './screens/settings';
import { Ionicons } from '@expo/vector-icons';
import { AuthProvider } from './components/AuthProvider';

import { useAuth } from './components/AuthProvider';

function HomeScreen() {
  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text>Home!</Text>
    </View>
  );
}



const Tab = createBottomTabNavigator();

function Tabs () {
  const { isAuthenticated, token } = useAuth();

  return (
      <Tab.Navigator>
        {
          (token != null) ? (
            <>
              <Tab.Screen name="Home" component={HomeScreen} />
              <Tab.Screen name="Message Log" component={MessageLog} />
              <Tab.Screen name="Settings" component={Settings} />
            </>
          ) : (
            <Tab.Screen name="Login" component={LoginScreen} />
          )
        
        }
      </Tab.Navigator>
  )
}
export default function App() {
  return (
    <AuthProvider>
      <NavigationContainer>
         <Tabs />
      </NavigationContainer>

     
    </AuthProvider>
  );
}