import { StyleSheet, Text, View, Button, useState, useEffect, TextInput } from 'react-native'
import React from 'react'

const SettingScreen = ({ navigation, route }) => {

  // const [value, setValue] = React.useState(route.a)
  // React.useEffect(() => {
  //   setValue(route.a)

  // }, [route.a]) // to nie potrzebne

  return (
    <View>
      <Text>SettingScreen</Text>
      <Text>{route.params?.a}</Text>
      <TextInput></TextInput>
      <Button title="zapisz trwale" > </Button>
      <Button title="wyczysc pamiec" />
    </View>
  )
}

export default SettingScreen

const styles = StyleSheet.create({})