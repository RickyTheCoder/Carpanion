import React from 'react';
import { TextInput, StyleSheet } from 'react-native';

export default function InputComponent({ placeholder, value, onChangeText }) {
    return (
        <TextInput
            style={styles.input}
            placeholder={placeholder}
            onChangeText={onChangeText}
        />
    )
}

export function PasswordInputComponent({ placeholder, value, onChangeText }) {
    return (
        <TextInput
            style={styles.input}
            placeholder={placeholder}
            onChangeText={onChangeText}
            secureTextEntry={true}
        />
    )
}

const styles = StyleSheet.create({
    input: {
        width: '100%',
        height: 50,
        padding: 10,
        borderRadius: 10,
        backgroundColor: '#E9E9E9',
    },
});