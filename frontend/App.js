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

export default function App() {
  const { isAuthenticated } = useAuth();
  return (
    <AuthProvider>

      <NavigationContainer>
        { !isAuthenticated ? (
          <Tab.Navigator>
          <Tab.Screen name="Video Feed" component={HomeScreen} 
          options={{
            tabBarIcon: ({ color, size }) => 
            (<Ionicons name="videocam" color={color} size={size} />),
          }}
          />
          <Tab.Screen name="Message Log" component={MessageLog} 
          options={{
            tabBarIcon: ({ color, size }) => 
            (<Ionicons name="chatbox" color={color} size={size} />),
          }}
          />
          <Tab.Screen name="Settings" component={Settings} 
          options={{
            tabBarIcon: ({ color, size }) => 
            (<Ionicons name="settings-sharp" color={color} size={size} />),
          }}
          />
        </Tab.Navigator>
        ) : (
          <LoginScreen />
        ) }
       
      </NavigationContainer>
    </AuthProvider>
  );
}