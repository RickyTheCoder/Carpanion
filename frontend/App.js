import * as React from 'react';
import { useState } from 'react';
import { Text, View, StyleSheet, Button, TouchableOpacity, TouchableHighlight } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import LoginScreen from './screens/login';
import MessageLog from './screens/messagelog';
import Settings from './screens/settings';
import { Ionicons } from '@expo/vector-icons';
import { Camera, CameraType } from 'expo-camera';


const Video = () => {
  const [type, setType] = useState(CameraType.back);
  
  const requestPermission = async () => {
    const cameraGranted = await requestPermissionCamera();
    const microphoneGranted = await requestPermissionMicrophone();
  };
  const [permissionCamera, requestPermissionCamera] = Camera.useCameraPermissions();
  const [permissionMicrophone, requestPermissionMicrophone] = Camera.useMicrophonePermissions();

  
  /* @hide if (!permission) ... */
  if (!permissionCamera || !permissionMicrophone) {
    // Camera permissions are still loading
    return <View />;
  }
  /* @end */

  /* @hide if (!permission.granted) ... */
  if (!permissionCamera.granted || !permissionMicrophone.granted) {
    // Camera permissions are not granted yet
    return (
      <View style={styles.container}>
        <Text style={{ textAlign: 'center', fontSize: 18 }}>Please grant video and audio permission.</Text>
        
        
        <TouchableOpacity 
          style={styles.grantButton} 
          onPress={requestPermission}>
          <Text style={styles.grantText}>Grant Permissions</Text>
        </TouchableOpacity>
      </View>
    );
  }
  /* @end */

  function toggleCameraType() {
    setType(current => (current === CameraType.back ? CameraType.front : CameraType.back));
  }

  return (
    <View>
      <Camera style={styles.camera} type={type}>
      <View>
      <TouchableOpacity onPress={toggleCameraType}>
          
            <Ionicons name="camera-reverse-outline" 
            size={40}
            style={{
              marginLeft: "90%",
              color: 'white'
              }}/>
            
          
      </TouchableOpacity>
      </View>
       {/*  <TouchableOpacity style={styles.grantButton} onPress={toggleCameraType}>
            <Text style={styles.grantText}>Flip Camera</Text>
        </TouchableOpacity> */}
      </Camera>
    </View>
    
  );
}

function HomeScreen() {
  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      
      <Video/>

    </View>
  );
}



const Tab = createBottomTabNavigator();

export default function App() {
  return (
    <NavigationContainer>
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
        <Tab.Screen name="Login" component={LoginScreen} />
      </Tab.Navigator>
    </NavigationContainer>
  );
}

const styles = StyleSheet.create({
  container: {
   
    justifyContent: 'center',
  },
  camera: {
    flex: 1,
  },
  buttonContainer: {
    flex: 1,
    flexDirection: 'row',
    backgroundColor: 'transparent',
    margin: 197,
  },
  button: {
    flex: 1,
    alignSelf: 'flex-end',
    alignItems: 'center',
  },
  text: {
    fontSize: 24,
    fontWeight: 'bold',
    color: 'white',
  },
  grantText: {
    fontSize: 18,
    color: "#fff",
    textAlign: 'center',
    paddingTop: 5,
    paddingBottom: 5,
    paddingRight: 15,
    paddingLeft: 15,
  },
  grantButton: {
    marginTop: 15,
    marginRight: 100,
    marginLeft: 100,
    backgroundColor:'dodgerblue',
    borderRadius: 15
  },
});