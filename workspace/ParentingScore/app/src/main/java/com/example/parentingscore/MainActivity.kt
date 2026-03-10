package com.example.parentingscore

import android.app.Activity
import android.os.Bundle
import android.content.Intent
import android.net.Uri
import android.provider.Settings
import android.util.Log

class MainActivity : Activity() {
    
    companion object {
        private const val TAG = "PARENTING"
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        
        // Direct logcat output
        Log.d(TAG, "========== onCreate START ==========")
        Log.d(TAG, "Package: $packageName")
        
        try {
            // Try simplest possible layout
            val textView = android.widget.TextView(this)
            textView.text = "Hello World! App is running."
            textView.textSize = 24f
            textView.setPadding(50, 50, 50, 50)
            setContentView(textView)
            
            Log.d(TAG, "Content view set successfully!")
            Log.d(TAG, "========== onCreate END ==========")
            
        } catch (e: Exception) {
            Log.e(TAG, "ERROR: ${e.message}")
            Log.e(TAG, "Stack: ${e.stackTrace}")
        }
    }
    
    override fun onStart() {
        super.onStart()
        Log.d(TAG, "onStart called")
    }
    
    override fun onResume() {
        super.onResume()
        Log.d(TAG, "onResume called")
    }
}
