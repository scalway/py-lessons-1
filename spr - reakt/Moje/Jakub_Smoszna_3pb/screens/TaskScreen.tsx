import { StyleSheet, Text, View, Button, TextInput, FlatList, TouchableOpacity } from 'react-native'
import React from 'react' 

const TaskScreen = ({ navigation }) => {

  const [value, setValue] = React.useState("tak")
  const [tasks, setTask] = React.useState([])

  // React.useEffect( async () => {

  //   const x = await fetch("http://localhost:3002/task", {})
  //   const json = await x.json()
  //   setTask(json)
  // }) to samo co nizej

  //   React.useEffect( () => {

  //   const x = fetch("http://localhost:3002/task", {})
  //   x.then((x) => {
  //     const json = x.json()
  //     json.then((json) => {
  //       setTask(json)
  //     })
  //   })
  // })
//127.0.0.1 to samo co localhost

  React.useEffect( () => {
  
    fetch("http://127.0.0.1:3002/task", {})
    .then((x) => x.json() )
    .then((x) => setTask(x))

  },[])

  return (

    <View>
      <TouchableOpacity >
        <TextInput placeholder="Tytul zadania" onChangeText={setValue} ></TextInput>
        <Button title="Dodaj" onPress={() => {
          // const x = tasks.slice()
          // x.push({key: value })
          setTask([...tasks,{key: value }])
          }}> </Button>
      </TouchableOpacity>

      <FlatList
        data={ tasks }

        renderItem={({ item }) => <TouchableOpacity><Text>{item.key}</Text><Button style={styles.container} title="kliknij aby zobacztc wiecej"></Button></TouchableOpacity>}
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