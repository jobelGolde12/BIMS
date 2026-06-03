# Database Documentation

## Tables

### Users
- `id`: Primary Key
- `username`: Unique username
- `password`: Plaintext password (admin/admin123)
- `role`: User role

### Residents
- `resident_id`: Unique identifier
- `first_name`, `middle_name`, `last_name`
- `gender`, `birthdate`, `age`, `civil_status`, `occupation`
- `address`, `contact_number`, `voter_status`
- `photo`: BLOB data
- `created_at`: Timestamp

### Households
- `household_id`: Unique identifier
- `head_name`: Name of household head
- `address`
- `members`: Number of members

### Officials
- `name`, `position`, `term_start`, `term_end`, `contact_number`

### Certificates
- `certificate_number`: Unique serial
- `resident_id`: Foreign Key to Residents
- `certificate_type`
- `issued_date`
