import { Pressable, StyleSheet, Text } from "react-native";

export default function ButtonComponent({ title, onPress }) {
    return (
        <Pressable onPress={onPress} style={styles.button}>
            <Text style={styles.text}>{title}</Text>
        </Pressable>
    )
}

const styles = StyleSheet.create({
    button: {
        backgroundColor: "#46A4D9",
        color: "white",
        padding: 12,
        borderRadius: 100,
        width: '100%',
    },
    text: {
        color: "white",
        textAlign: "center",
    }
});