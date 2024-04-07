import React, { useState } from 'react';
import { TouchableOpacity, Text, View, TextInput, Button, Alert, StyleSheet } from 'react-native';

import { useNavigation } from '@react-navigation/native'; 
import { useAuth } from '../components/AuthProvider';


export default function ChangePassword() {
  const navigation = useNavigation();
  const [currentPassword, setCurrentPassword] = useState('');
  const [newPassword, setNewPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const { token } = useAuth();

  const handleChangePassword = async () => {
    // Validate if the new password matches the confirm password
    if (newPassword !== confirmPassword) {
      Alert.alert('Error', 'Passwords do not match.');
      return;
    }

    const res = await fetch('http://10.103.232.163:8000/api/v1/auth/password/change/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Token ' + token,
      },
      body: JSON.stringify({ old_password: currentPassword, new_password1: newPassword, new_password2: confirmPassword }),
    })

    if (!res.ok) {
      Alert.alert('Error', 'Failed to change password.');
      return;
    }
    
    Alert.alert('Success', 'Password changed successfully.', [
      {
        text: 'OK',
        onPress: () => {
          // Clear input fields after successful password change
          setCurrentPassword('');
          setNewPassword('');
          setConfirmPassword('');

          // Navigate back to previous screen
          navigation.goBack();
        }
      }
    ]);
  };

  return (
    <View style={styles.container}>
      <Text style={styles.inputTitle}>Current Password</Text>
      <TextInput
        style={styles.input}
        placeholder=""
        secureTextEntry={true}
        value={currentPassword}
        onChangeText={setCurrentPassword}
      />
      <Text style={styles.inputTitle}>{token}New Password</Text>
      <TextInput
        style={styles.input}
        placeholder=""
        secureTextEntry={true}
        value={newPassword}
        onChangeText={setNewPassword}
      />
      <Text style={styles.inputTitle}>Confirm New Password</Text>
      <TextInput
        style={styles.input}
        placeholder=""
        secureTextEntry={true}
        value={confirmPassword}
        onChangeText={setConfirmPassword}
      />
      {/* <Button title="Change Password" onPress={handleChangePas }sword} />*/}
      <TouchableOpacity
          style={styles.changeButton}
          onPress={handleChangePassword}
          underlayColor='#fff'>
          <View>
            <Text style={styles.changeText}>Change Password</Text>
          </View>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    backgroundColor: 'rgba(255,255,255,0.9)',
    flex: 1,
    alignItems: 'center',
    paddingHorizontal: 20,
  },
  inputTitle: {
    fontSize: 17,
    alignSelf: 'left',
    marginLeft: 6,
    paddingVertical: 15,
  },
  input: {
    backgroundColor: 'rgba(255,255,255,0.6)',
    width: '100%',
    marginBottom: 10,
    paddingHorizontal: 10,
    paddingVertical: 8,
    borderWidth: 1,
    borderColor: '#ccc',
    borderRadius: 5,
  },
  changeText: {
    fontSize: 17,
    color: "#fff",
    textAlign: 'center',
    paddingVertical: 7,
    paddingHorizontal: 15,
  },
  changeButton: {
    marginTop: 15,
    marginRight: 75,
    marginLeft: 75,
    marginBottom: 15,
    backgroundColor:'dodgerblue',
    borderRadius: 15
  },
});