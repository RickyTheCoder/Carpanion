import { Text, StyleSheet } from "react-native";

export function P({ text }) {
    return (
        <Text
            style={styles.p}
        >
            {text}
        </Text>
    )
}

export function H1({ text }) {
    return (
        <Text
        style={styles.h1}
    >
        {text}
    </Text>
    )
}

export function H2({ text }) {
    return (
        <Text
        style={styles.h1}
    >
        {text}
    </Text>
    )
}

const styles = StyleSheet.create({
    h1: {
        fontSize: 48,
        fontWeight: '600',
    },
    h2: {
        fontSize: 20,
    },
    p: {
        fontSize: 16,
    }
});