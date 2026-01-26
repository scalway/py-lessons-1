import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { NavigationContainer } from '@react-navigation/native';
import { SafeAreaView } from 'react-native-safe-area-context';
import Task from './Screens/Task';
import Settings from './Screens/Settings';

const Stack = createNativeStackNavigator()

export default function App() {
  return (
    <NavigationContainer>
      <SafeAreaView style={{flex:1}}>
        <Stack.Navigator>
          <Stack.Screen name='Tasks' component={Task} options={{
            title:'Tasks',
            headerStyle:{
              backgroundColor:'#bbff'
            }
          }}></Stack.Screen>
          <Stack.Screen name='Settings' component={Settings} options={{
            title:'Settings',
            headerStyle:{
              backgroundColor:'#bbff'
            }
          }}></Stack.Screen>
        </Stack.Navigator>
      </SafeAreaView>
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
