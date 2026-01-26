import { StyleSheet, Text, View, FlatList, TouchableOpacity, KeyboardAvoidingView, TextInput, Platform, Alert } from 'react-native'
import React, { useEffect, useState } from 'react'
import TaskItem from '../components/TaskItem'
import * as SecureStore from 'expo-secure-store'
import Details from '../components/Details'

const Task = ({ navigation }) => {
    const [tasks, setTasks] = useState()
    const [title, setTitle] = useState()
    const [show, setShow] = useState(false)
    const [detTit, setDettit] = useState()
    const [detDesc, setDetDesc] = useState()
    
    useEffect(() => {
        fetch('http://192.168.119.111:3001/tasks').then(res => res.json()).then(data => {
            setTasks(data)
        })
    }, [navigation])
    const addTask = async () => {
        const value = await SecureStore.getItemAsync('keyToUnlock')
        if (value) {
            fetch('http://192.168.119.111:3001/add', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    title: title,
                    description: `Użyto klucza ${value}`
                })
            })
            fetch('http://192.168.119.111:3001/tasks').then(res => res.json()).then(data => {
                setTasks(data)
            })
        }
        else {
            Alert.alert('Error', 'Brak klucza zapisu', [
                {
                    text: 'OK',
                    onPress: () => { }
                }
            ], {
                cancelable: true,
                onDismiss: () => { }
            })
        }

    }
    const showDetails = async(title, desc) => {
        setShow(true)
        setDettit(title)
        setDetDesc(desc)
        const value = await SecureStore.getItemAsync('keyToUnlock')

    }
    return (
        <View style={styles.container}>
            <KeyboardAvoidingView behavior={Platform.OS === 'ios' ? 'padding' : 'height'} style={{ flex: 0, flexDirection: 'row' }}>
                <TextInput onChangeText={setTitle} value={title} style={{ backgroundColor: '#eee', width: 200, paddind: 20, margin: 10, borderBottomColor: 'black', borderBottomWidth: 2 }} placeholder='Tytuł zadania'></TextInput>
                <TouchableOpacity style={styles.buttonD} onPress={() => addTask()}><Text style={{ color: 'white' }}>Dodaj</Text></TouchableOpacity>
            </KeyboardAvoidingView>
            {show && (
                <Details title={detTit} description={detDesc} />
            )}
            <FlatList
                data={tasks}
                renderItem={({ item, index }) => <TaskItem title={item.title} description={item.description} key={index} showDetails={() => showDetails(item.title, item.description)} />}
            />
            <TouchableOpacity style={styles.button} onPress={() => navigation.navigate('Settings')}><Text style={{ color: 'white' }}>Konfiguruj klucz</Text></TouchableOpacity>
        </View>
    )
}

export default Task

const styles = StyleSheet.create({
    container: {
        flex: 1,
        justifyContent: 'center',
        padding: 10,
        alignItems: 'center'
    },
    button: {
        padding: 20,
        borderRadius: 20,
        backgroundColor: '#00abcf',
        margin: 10,
        width: 190
    },
    buttonD: {
        padding: 10,
        borderRadius: 20,
        backgroundColor: '#00abcf',
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        width: 100
    }
})