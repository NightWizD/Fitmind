import React, { useEffect, useRef } from 'react';
import { View, Text, Animated } from 'react-native';

const SplashScreen = ({ navigation }) => {
  const fadeAnim = useRef(new Animated.Value(0)).current;

  useEffect(() => {
    Animated.timing(fadeAnim, {
      toValue: 1,
      duration: 1000,
      useNativeDriver: true,
    }).start();

    const timer = setTimeout(() => {
      navigation.navigate('Login');
    }, 2000);

    return () => clearTimeout(timer);
  }, [fadeAnim, navigation]);

  return (
    <View className="flex-1 bg-slate-900 justify-center items-center">
      <Animated.View style={{ opacity: fadeAnim }}>
        <Text className="text-white text-4xl font-bold mb-4">FitMind AI</Text>
        <Text className="text-gray-300 text-lg text-center">Your Intelligent Fitness Partner</Text>
      </Animated.View>
    </View>
  );
};

export default SplashScreen;
