import React, { Component } from 'react';
import { View, Text, Button, StyleSheet } from 'react-native';
import Geolocation from '@react-native-community/geolocation';

class App extends Component {
  constructor() {
    super();
    this.state = {
      latitude: null,
      longitude: null,
      error: null,
    };
  }

  componentDidMount() {
    Geolocation.getCurrentPosition(
      (position) => {
        const { latitude, longitude } = position.coords;
        this.setState({
          latitude,
          longitude,
          error: null,
        });
      },
      (error) => this.setState({ error: error.message }),
      { enableHighAccuracy: true, timeout: 20000, maximumAge: 1000 }
    );
  }

  render() {
    return (
      <View style={styles.container}>
        <View style={styles.quadrado}>
        <Text style={styles.texto}t>Latitude: {this.state.latitude}</Text>
        <Text style={styles.texto}>Longitude: {this.state.longitude}</Text>
        {this.state.error ? (
          <Text>Error: {this.state.error}</Text>
        ) : null}
        <Button
          title="Get Location"
          onPress={() => this.componentDidMount()}
        />
        </View>
      </View>
    );
  }
}

export default App;

const styles = StyleSheet.create({
  container: {
    alignItems: 'center',
    justifyContent: 'center',
    flex: 1,
    backgroundColor: '#E6E4E4'
  },
  texto: {
    margin: '8px',
    fontWeight: 600,
    textAlign: 'center'
  },
  quadrado: {
    width: '200px',
    backgroundColor: 'white'
  }
  

})
