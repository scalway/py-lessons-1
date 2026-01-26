import { View, Text,StyleSheet } from 'react-native'
import React from 'react'

const Details = ({title,description,close}) => {
  return (
    <View style={styles.task}>
      <Text style={styles.title}>{title}</Text>
      <Text style={styles.desc}>{description}</Text>
    </View>
  )
}

export default Details

const styles = StyleSheet.create({
    task:{
        flex:1,
        padding:20,
        backgroundColor:'#00bbee',
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