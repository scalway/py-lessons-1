import { StyleSheet, Text, View, Button, useState, useEffect, TextInput, FlatList, TouchableOpacity } from 'react-native'
import React from 'react'

const TaskScreen = ({ navigation }) => {

  const [value, setValue] = React.useState("tak")
  return (

    <View>
      <TouchableOpacity >
        <TextInput placeholder="Tytul zadania" onChangeText={setValue} ></TextInput>
        <Button title="Dodaj" > </Button>
      </TouchableOpacity>

      <FlatList
        data={
          [
            { key: 'Nauczyc sie reakta' },
            { key: 'Ajesc obiad' },
          ]
        }

        renderItem={({ item }) => <TouchableOpacity > <Text>{item.key}</Text> <Button style={styles.container} title="kliknij aby zobacztc wiecej" > </Button></TouchableOpacity>}
      />

      <Button title="klik" onPress={() => { navigation.navigate("Ustawienie zabezpieczen", { a: value }) }} />
    </View>
  )
}

export default TaskScreen

const styles = StyleSheet.create({

  container: {
    flex: 1,
    backgroundColor: "#FF0000",
    justifyContent: 'center',
  },
  bt: {
    backgroundColor: "#FFFFFF",
  },

})