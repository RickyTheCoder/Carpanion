import React, { useState } from 'react';
import { Alert, Modal, Pressable, StyleSheet, Text, View, TouchableOpacity } from 'react-native';
import { Dropdown, MultiSelect } from 'react-native-element-dropdown';
import { useNavigation } from '@react-navigation/native'; 
import LoginScreen from './login.jsx';
import { EvilIcons } from '@expo/vector-icons';
import { useAuth } from '../components/AuthProvider.jsx';

  const dataVoice = [
    { label: 'British Male', value: 'britishmale' },
    { label: 'British Female', value: 'britishfemale' },
  ];

  const DropdownVoice = () => {
    const [value, setValue] = useState(null);
    const [isFocus, setIsFocus] = useState(false);

    const renderLabel = () => {
      if (value || isFocus) {
        return (
          <Text style={[styles.label, isFocus && { color: 'dodgerblue' }]}>
            Voice
          </Text>
        );
      }
      return null;
    };

    return (
      <View style={styles.container}>
        {renderLabel()}
        <Dropdown
          style={[styles.dropdown, isFocus && { borderColor: 'dodgerblue' }]}
          placeholderStyle={styles.placeholderStyle}
          selectedTextStyle={styles.selectedTextStyle}
          data={dataVoice}
          maxHeight={300}
          labelField="label"
          valueField="value"
          placeholder={!isFocus ? 'Select voice' : '...'}
          value={value}
          onFocus={() => setIsFocus(true)}
          onBlur={() => setIsFocus(false)}
          onChange={item => {
            setValue(item.value);
            setIsFocus(false);
          }}
        />
      </View>
    );
  };



  const dataPersonality = [
    { label: 'Happy', value: 'happy' },
    { label: 'Sad', value: 'sad' },
  ];

  const DropdownPersonality = () => {
    const [value, setValue] = useState(null);
    const [isFocus, setIsFocus] = useState(false);

    const renderLabel = () => {
      if (value || isFocus) {
        return (
          <Text style={[styles.label, isFocus && { color: 'dodgerblue' }]}>
            Personality
          </Text>
        );
      }
      return null;
    };

    return (
      <View style={styles.container}>
        {renderLabel()}
        <Dropdown
          style={[styles.dropdown, isFocus && { borderColor: 'dodgerblue' }]}
          placeholderStyle={styles.placeholderStyle}
          selectedTextStyle={styles.selectedTextStyle}
          data={dataPersonality}
          maxHeight={300}
          labelField="label"
          valueField="value"
          placeholder={!isFocus ? 'Select personality' : '...'}
          value={value}
          onFocus={() => setIsFocus(true)}
          onBlur={() => setIsFocus(false)}
          onChange={item => {
            setValue(item.value);
            setIsFocus(false);
          }}
        />
      </View>
    );
  };

  const dataHobbies = [
    { label: 'Chess', value: 'chess' },
    { label: 'Reading', value: 'reading' },
    { label: 'Dancing', value: 'dancing' },
    { label: 'Running', value: 'running' },
  ];

  const MultiSelectComponent = () => {
    const [selected, setSelected] = useState([]);

    return (
      <View style={styles.container}>
        <MultiSelect
          style={styles.dropdownMultiSelect}
          placeholderStyle={styles.placeholderStyle}
          selectedTextStyle={styles.selectedTextStyle}
          data={dataHobbies}
          labelField="label"
          valueField="value"
          placeholder="Edit hobbies"
          value={selected}
          onChange={item => {
            setSelected(item);
          }}
          selectedStyle={styles.selectedStyle}
        />
      </View>
    );
  };

  const LogoutScreen = () => {
    const navigation = useNavigation();
    const { logout } = useAuth();
  
    const handleLogout = () => {
      

      
      navigation.replace('Login'); 

      logout();

    };
  
    return (
      <View>
        <TouchableOpacity
          style={styles.logoutButton}
          onPress={handleLogout}
          underlayColor='#fff'>
          <Text style={styles.logoutText}>Logout</Text>
        </TouchableOpacity>
      </View>
    );
  };

  const ChangePword = () => {
    const navigation = useNavigation();
  
    const handleChangePassword = () => {
      
      navigation.navigate('Change Password'); 
    };
  
    return (
      <View>
        <TouchableOpacity
          style={styles.passwordButton}
          onPress={handleChangePassword}
          underlayColor='#fff'>
          <View style={{flexDirection:"row"}}>
            <Text style={styles.passwordText}>Change Password</Text>
            <EvilIcons style={{marginLeft: 192, marginTop: 13}}name="chevron-right" size={28} color="rgba(0,0,0,0.6)" />
          </View>
        </TouchableOpacity>
      </View>
    );
  };

 



  export default function Settings ()
  {
    return (
    <View style={{backgroundColor:'white'}}>
      <DropdownVoice/>
      <DropdownPersonality/>
      <MultiSelectComponent/>
      <ChangePword/>
      <LogoutScreen/>
      

    </View>
    );
  }
  //export default DropdownComponent;

  const styles = StyleSheet.create({
    container: {
      backgroundColor: 'white',
      padding: 16,
    },
    dropdownMultiSelect: {
      height: 50,
      backgroundColor: 'transparent',
      marginTop: 0,
      borderBottomColor: 'gray',
      borderBottomWidth: 0.5,
    },
    dropdown: {
      backgroundColor: 'white',
      height: 50,
      borderColor: 'gray',
      borderWidth: 0.5,
      borderRadius: 8,
      paddingHorizontal: 8,
    },
    label: {
      position: 'absolute',
      backgroundColor: 'white',
      left: 22,
      top: 8,
      zIndex: 999,
      paddingHorizontal: 8,
      fontSize: 14,
    },
    placeholderStyle: {
      fontSize: 16,
    },
    selectedTextStyle: {
      fontSize: 16,
    },
    logoutText: {
      fontSize: 17,
      color: "#fff",
      textAlign: 'center',
      paddingTop: 5,
      paddingBottom: 5
    },
    logoutButton: {
      marginTop: 15,
      marginRight: 155,
      marginLeft: 155,
      marginBottom: 15,
      backgroundColor:'dodgerblue',
      borderRadius: 15
    },

    passwordText: {
      fontSize: 16,
      textAlign: 'left',
      paddingTop: 15,
      paddingBottom: 10
    
    },
    passwordButton: {
      /* marginTop: 15,
      marginRight: 155,
      marginLeft: 155,
      backgroundColor:'white',
      borderRadius: 15 */
      marginTop: 16,
      marginBottom: 17,
      backgroundColor: 'white',
      height: 50,
      borderColor: 'gray',
      borderWidth: 0.5,
      borderRadius: 8,
      paddingHorizontal: 10,
      marginLeft: 15,
      marginRight: 15,
    },

    centeredView: {
      flex: 1,
      justifyContent: 'center',
      alignItems: 'center',
      marginTop: 22,
    },
    modalView: {
      margin: 20,
      backgroundColor: 'white',
      borderRadius: 20,
      padding: 35,
      alignItems: 'center',
      shadowColor: '#000',
      shadowOffset: {
        width: 0,
        height: 2,
      },
      shadowOpacity: 0.25,
      shadowRadius: 4,
      elevation: 5,
    },
    button: {
      backgroundColor: "black",
      borderRadius: 20,
      padding: 10,
      elevation: 2,
    },
    buttonOpen: {
      backgroundColor: '#F194FF',
    },
    buttonClose: {
      backgroundColor: '#2196F3',
    },
    textStyle: {
      color: 'white',
      fontWeight: 'bold',
      textAlign: 'center',
    },
    modalText: {
      marginBottom: 15,
      textAlign: 'center',
    },
  });

/*

import React, { useState } from 'react';
import RNPickerSelect from 'react-native-picker-select';
//import {Picker} from '@react-native-picker/picker';
import { View, Text } from 'react-native';


export default function Settings ()
{
  const [selectedVoice, setSelectedVoice] = useState(null);

  const placeholder = {
    label: 'Select option',
    value: null,
  };

  const options = [
    { label: 'Option 1', value: 'option1' },
    { label: 'Option 2', value: 'option2' },
    { label: 'Option 3', value: 'option3' },
  ];

  return (
    <View>
      <Text>Select an option:</Text>
      <RNPickerSelect
        placeholder={placeholder}
        items={options}
        onValueChange={(value) => setSelectedVoice(value)}
        value={selectedVoice}
      />
      {selectedVoice && <Text>Selected: {selectedVoice}</Text>}
    </View>
  );
  /*
  //const [selectedVoice, setSelectedVoice] = useState();
  return (
    <Picker
        selectedValue={selectedVoice}
        onValueChange={(itemValue, itemIndex) =>
          setSelectedVoice(itemValue)
        }>
        <Picker.Item label="British Male" value="britishmale" />
        <Picker.Item label="British Female" value="britishfemale" />
    </Picker> 
  );
  
} */

import React from 'react';
import ImageUploader from '../components/ImageUploader';

const SettingsScreen = () => {
  return (
    <div>
      <ImageUploader />
    </div>
  );
};

