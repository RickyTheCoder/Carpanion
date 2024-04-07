import * as React from 'react';
import { useState } from 'react';
import { Text, View, StyleSheet, Button, TouchableOpacity, TouchableHighlight } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import LoginScreen from './screens/login';
import MessageLog from './screens/messagelog';
import Settings from './screens/settings';
import ChangePassword from './screens/changepassword'
import { Ionicons } from '@expo/vector-icons';
import { Camera, CameraType } from 'expo-camera';
import { cameraWithTensors } from '@tensorflow/tfjs-react-native';

const TensorCamera = cameraWithTensors(Camera);


const handleCameraStream = (images, updatePreview, gl) => {
  const loop = async () => {
    const nextImageTensor = images.next().value

    console.log(images)
    

    // send image to api backend

    const response = await fetch('http://10.103.232.163:8000/ai/image_to_text/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ image: nextImageTensor }),
    });
    

    // do something with the response
    const data = await response.json();
    console.log(data);

    // if autorender is false you need the following two lines.
    // updatePreview();
    // gl.endFrameEXP();

    requestAnimationFrame(loop);
  }
  setInterval(loop, 4000);
}


const Video = () => {
  const cameraRef = React.useRef(null);
  const [type, setType] = useState(CameraType.back);
  
  const requestPermission = async () => {
    const cameraGranted = await requestPermissionCamera();
    const microphoneGranted = await requestPermissionMicrophone();
  };
  const [permissionCamera, requestPermissionCamera] = Camera.useCameraPermissions();
  const [permissionMicrophone, requestPermissionMicrophone] = Camera.useMicrophonePermissions();

  React.useEffect(() => {
    const takePhoto = async () => {
      if (cameraRef.current) {
        let photo = await cameraRef.current.takePictureAsync({
          base64: true,
        });


        // send photo to api backend

        const response = await fetch('http://10.103.232.163:8000/ai/image_to_text/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ image: photo.base64 }),
        });

        // do something with the response

      }
    }

    setInterval(takePhoto, 5000);
  })

  
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
    setType(current => (current === Camera.Constants.Type.back ? Camera.Constants.Type.front : Camera.Constants.Type.back));
  }

  return (
    
    <View>
      <Camera ref={cameraRef} style={styles.camera} type={type}
      
      >

      <View>
    
      <TouchableOpacity onPress={toggleCameraType}>
          
        <Ionicons name="camera-reverse-outline" 
        size={40}
        style={{
          marginLeft: "90%",
          color: 'black',
          
          }}/>
      </TouchableOpacity>
      </View> 
      </Camera>
      
      
      
       {/*  <TouchableOpacity style={styles.grantButton} onPress={toggleCameraType}>
            <Text style={styles.grantText}>Flip Camera</Text>
        </TouchableOpacity> */}
      
    </View>
    
  );
}
import { AuthProvider } from './components/AuthProvider';

import { useAuth } from './components/AuthProvider';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import RegisterScreen from './screens/register';

function HomeScreen() {
  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      
      <Video/>

    </View>
  );
}



const Tab = createBottomTabNavigator();
const Stack = createNativeStackNavigator();

function HomeTabs () {
  const { isAuthenticated, token } = useAuth();

  return (
      <Tab.Navigator>
        {
          (token != null) ? (
            <>
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
            </>
          ) : (
            <>
            <Tab.Screen name="Login" component={LoginScreen} />
            <Tab.Screen name="Register" component={RegisterScreen} />
            </>
          )
        
        }
      </Tab.Navigator>
  )
}

export default function App() {
  return (
    <AuthProvider>
    <NavigationContainer>
    <Stack.Navigator >
      <Stack.Screen name="Home" component={HomeTabs} options={{headerShown: false}}/>
      <Stack.Screen name="Change Password" component={ChangePassword} options={{ headerBackTitle: 'Back' }}/>
      <Stack.Screen name="Login" 
      component={LoginScreen} 
      options={{headerBackTitle: 'Back', headerBackTitleStyle: {fontSize: 30,}}}/>  
       
    </Stack.Navigator>
    </NavigationContainer>
    </AuthProvider>
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