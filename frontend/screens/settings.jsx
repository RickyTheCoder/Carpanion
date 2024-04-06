import React, { useState } from 'react';
import { StyleSheet, Text, View } from 'react-native';
import { Dropdown, MultiSelect } from 'react-native-element-dropdown';

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
          <Text style={[styles.label, isFocus && { color: 'blue' }]}>
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
          style={[styles.dropdown, isFocus && { borderColor: 'blue' }]}
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
          <Text style={[styles.label, isFocus && { color: 'blue' }]}>
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
          style={[styles.dropdown, isFocus && { borderColor: 'blue' }]}
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
          style={styles.dropdown}
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

  export default function MessageLog ()
  {
    return (
    <View>
      <DropdownVoice/>
      <DropdownPersonality/>
      <MultiSelectComponent/>
    </View>
    );
  }
  //export default DropdownComponent;

  const styles = StyleSheet.create({
    container: {
      backgroundColor: 'white',
      padding: 16,
    },
    dropdown: {
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
