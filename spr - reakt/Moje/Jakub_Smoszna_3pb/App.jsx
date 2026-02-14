import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Button, useState, useEffect } from 'react-native';
import * as React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import SettingScreen from "./screens/SettingScreen"
import TaskScreen from "./screens/TaskScreen"


const Stack = createNativeStackNavigator();

export default function App() {

  const [value, setValue] = React.useState("tak")

  React.useEffect(() => {

    fetch("https://jsonplaceholder.typicode.com/posts/3", {})
      .then(response => response.json())
      .then(data => {
        console.log(data);
        setValue((value) => value + data.title)
      })

  }, [])



  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen name="Lista zadań" component={TaskScreen} />
        <Stack.Screen name="Ustawienie zabezpieczen" component={SettingScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
