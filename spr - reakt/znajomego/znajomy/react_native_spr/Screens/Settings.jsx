import { StyleSheet, Text, View, TextInput, KeyboardAvoidingView, Platform, TouchableOpacity, Alert } from 'react-native'
import React, { useEffect, useState } from 'react'
import * as SecureStore from 'expo-secure-store'

const Settings = ({ navigation }) => {
    const [currKey, setCurrKey] = useState("")
    useEffect(() => {
        const fetchkey = async () => {
            const value = await SecureStore.getItemAsync('keyToUnlock')
            if (value) {
                setCurrKey(value)
            }
            else {
                setCurrKey("")
            }
        }
        fetchkey()
    }, [navigation])
    const save = async () => {
        await SecureStore.setItemAsync('keyToUnlock', currKey)
        Alert.alert('Success', 'Zapisano klucz, powrót do ekranu zadań', [
            {
                text: 'OK',
                onPress: () => { }
            }
        ], {
            cancelable: true,
            onDismiss: () => { }
        })
        navigation.navigate('Tasks')
    }
    const clear = async () => {
        await SecureStore.deleteItemAsync('keyToUnlock')
        Alert.alert('Warning', 'Wyczyszczono pamięć, powrót do ekranu zadań', [
            {
                text: 'OK',
                onPress: () => { }
            }
        ], {
            cancelable: true,
            onDismiss: () => { }
        })
        navigation.navigate('Tasks')
    }
    return (
        <View style={styles.container}>
            <Text>Wartość w Secure Store</Text>
            <Text>{currKey}</Text>
            <KeyboardAvoidingView behavior={Platform.OS === 'ios' ? 'padding' : 'height'}>
                <TextInput onChangeText={setCurrKey} value={currKey} style={{ backgroundColor: '#eee', width: 200, paddind: 20, margin: 10, borderBottomColor: 'black', borderBottomWidth: 2 }} placeholder='Wartość klucza zapisu'></TextInput>
            </KeyboardAvoidingView>
            <TouchableOpacity style={[styles.button, { backgroundColor: '#00df66' }]} onPress={() => save()}><Text style={{ color: 'white' }}>Zapisz trwawle</Text></TouchableOpacity>
            <TouchableOpacity style={[styles.button, { backgroundColor: '#dd0000' }]} onPress={() => clear()}><Text style={{ color: 'white' }}>Wyczyść pamięć</Text></TouchableOpacity>
        </View>
    )
}

export default Settings

const styles = StyleSheet.create({
    container: {
        flex: 1,
        padding: 10,
        alignItems: 'center'
    },
    button: {
        padding: 20,
        borderRadius: 20,
        margin: 10,
        width: 180,
        justifyContent: 'center',
        alignItems: 'center'
    }
})