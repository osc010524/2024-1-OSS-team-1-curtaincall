import {createTheme} from "@mui/material";

export const FIBTheme = createTheme({
    components: {
        MuiButton: {
            styleOverrides: {
                root: {
                    width: '33.33%',
                    height: '70px',
                    borderRadius: '50px',
                    fontWeight: 'bold',
                    fontSize: '1.25rem',
                    position: 'relative',
                    transition: 'background-color 0.5s ease',
                    marginLeft: '0.25%',
                    '@media (max-width: 768px)': {
                        width: '66.6%',
                        marginTop: '0.25%',
                    },
                    backgroundColor: '#595959',
                    color: 'white',
                    '&:hover': {
                        backgroundColor: '#adadad'
                    }
                },
            }
        }
    }
});