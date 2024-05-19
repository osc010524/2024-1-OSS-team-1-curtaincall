import React from 'react';
import { TextField, ThemeProvider } from '@mui/material';
import { IIFTheme } from './Theme/IIFTheme'; // Import the custom theme for UsernameInput

function IDInputForm({ username, onUsernameChange }) {
    return (
        <ThemeProvider theme={IIFTheme}>
            <TextField
                hiddenLabel
                variant="outlined"
                placeholder="Username"
                value={username}
                onChange={(e) => onUsernameChange(e.target.value)}
                fullWidth
            />
        </ThemeProvider>
    );
}

export default IDInputForm;