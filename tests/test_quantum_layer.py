import unittest
import numpy as np
import sys
import os

# 添加src目录到Python路径
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from quantum_layer import QuantumLayer

class TestQuantumLayer(unittest.TestCase):
    """量子层测试类"""
    
    def setUp(self):
        """测试前初始化"""
        self.quantum = QuantumLayer()
        self.test_data = np.array([1, 2, 3, 4, 5])
        
    def test_quantum_state_exploration(self):
        """测试量子状态探索功能"""
        states = self.quantum.quantum_state_exploration(self.test_data)
        self.assertEqual(len(states), 10)  # 验证生成了10个状态
        for state in states:
            self.assertEqual(len(state), len(self.test_data))  # 验证状态维度
            
    def test_entangle_states(self):
        """测试量子纠缠功能"""
        state1 = np.array([1, 2, 3])
        state2 = np.array([4, 5, 6])
        entangled1, entangled2 = self.quantum.entangle_states(state1, state2)
        np.testing.assert_array_equal(entangled1, entangled2)  # 验证纠缠态

if __name__ == '__main__':
    unittest.main()
