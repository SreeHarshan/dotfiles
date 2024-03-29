/*
 * This file is part of mpv.
 *
 * mpv is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 *
 * mpv is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with mpv.  If not, see <http://www.gnu.org/licenses/>.
 */

#include <windows.h>

#include "osdep/path.h"
#include "osdep/io.h"
#include "options/path.h"

// Missing from MinGW headers.
WINBASEAPI DWORD WINAPI GetCurrentDirectoryW(DWORD nBufferLength, LPWSTR lpBuffer);

const char *mp_get_platform_path_uwp(void *talloc_ctx, const char *type)
{
    if (strcmp(type, "home") == 0) {
        DWORD count = GetCurrentDirectoryW(0, NULL);
        wchar_t *home_dir = talloc_array(NULL, wchar_t, count);
        if (GetCurrentDirectoryW(count, home_dir) != 0) {
            char *ret = mp_to_utf8(talloc_ctx, home_dir);
            talloc_free(home_dir);
            return ret;
        }
    }
    return NULL;
}
