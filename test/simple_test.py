#!/usr/bin/env python3
"""
Simple test script for Optimus package that doesn't require pandas.
"""

def test_basic_import():
    """Test basic import of optimus package."""
    print("🧪 Testing Basic Optimus Import")
    print("=" * 40)
    
    try:
        from optimus import ChemicalAnalyzer
        print("✅ Successfully imported ChemicalAnalyzer")
        
        analyzer = ChemicalAnalyzer()
        print("✅ Successfully created analyzer instance")
        
        return True
    except Exception as e:
        print(f"❌ Import failed: {e}")
        return False

def test_simple_analysis():
    """Test simple analysis without pandas."""
    print("\n🔬 Testing Simple Analysis")
    print("=" * 40)
    
    try:
        from optimus import ChemicalAnalyzer
        
        analyzer = ChemicalAnalyzer()
        
        # Test with ethanol (simple molecule)
        result = analyzer.analyze_smiles("CCO")
        
        print(f"✅ Analyzed ethanol (CCO)")
        print(f"   Molecular Weight: {result.molecular_weight:.2f} Da")
        print(f"   LogP: {result.logp:.2f}")
        print(f"   TPSA: {result.tpsa:.1f} Ų")
        print(f"   HBD: {result.hbd_count}")
        print(f"   HBA: {result.hba_count}")
        print(f"   Drug-likeness Score: {result.drug_likeness_score:.3f}")
        print(f"   Lipinski Pass: {result.lipinski.passed if result.lipinski else 'N/A'}")
        
        # Test with aspirin
        result2 = analyzer.analyze_smiles("CC(=O)OC1=CC=CC=C1C(=O)O")
        print(f"\n✅ Analyzed aspirin")
        print(f"   Molecular Weight: {result2.molecular_weight:.2f} Da")
        print(f"   LogP: {result2.logp:.2f}")
        print(f"   Drug-likeness Score: {result2.drug_likeness_score:.3f}")
        print(f"   Total Violations: {result2.total_violations}")
        
        return True
        
    except Exception as e:
        print(f"❌ Analysis failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_all_rules():
    """Test all ADMET rules."""
    print("\n📋 Testing All ADMET Rules")
    print("=" * 40)
    
    try:
        from optimus import ChemicalAnalyzer
        
        analyzer = ChemicalAnalyzer()
        result = analyzer.analyze_smiles("CC(=O)OC1=CC=CC=C1C(=O)O")  # Aspirin
        
        print("Rules analysis for Aspirin:")
        for rule_name, rule_result in result.rules.items():
            status = "✅ PASS" if rule_result.passed else "❌ FAIL"
            print(f"  {rule_result.name}: {status}")
        
        print(f"\nOverall Assessment:")
        print(f"  Drug-likeness Score: {result.drug_likeness_score:.3f}")
        print(f"  Is Drug-like: {'Yes' if result.is_drug_like() else 'No'}")
        print(f"  Total Violations: {result.total_violations}")
        
        return True
        
    except Exception as e:
        print(f"❌ Rules test failed: {e}")
        return False

if __name__ == '__main__':
    success = True
    
    success &= test_basic_import()
    success &= test_simple_analysis()
    success &= test_all_rules()
    
    if success:
        print("\n🎉 All basic tests passed!")
        print("\nOptimus is working correctly.")
        print("\nTo install missing dependencies:")
        print("  pip install pandas matplotlib seaborn tqdm click")
    else:
        print("\n❌ Some tests failed.")
        print("Please check the error messages above.")