import { View, Text,StyleSheet,TouchableOpacity } from 'react-native'
import React from 'react'

const TaskItem = ({title,description,showDetails}) => {
  return (
    <TouchableOpacity style={styles.task} onPress={()=>showDetails()}>
      <Text style={styles.title}>{title}</Text>
      <Text style={styles.desc}>{description}</Text>
    </TouchableOpacity>
  )
}

export default TaskItem

const styles = StyleSheet.create({
    task:{
        flex:1,
        padding:20,
        backgroundColor:'#1a1a1a',
        margin:10,
        borderRadius:20
    },
    title:{
        color:'white',
        fontSize:17
    },
    desc:{
        color:'white',
        fontSize:15
    }
})